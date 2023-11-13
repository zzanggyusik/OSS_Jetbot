# 필요한 라이브러리 import
import matplotlib.pyplot as plt
import numpy as np
import os, re, glob
import cv2
from sklearn.model_selection import train_test_split
import tensorflow as tf
keras = tf.keras
from keras.models import Sequential
from keras.layers import Dropout, Activation, Dense, BatchNormalization
from keras.layers import Flatten, Convolution2D, MaxPooling2D
from keras.models import load_model
from keras import layers, optimizers
from keras.callbacks import ModelCheckpoint
from tensorflow import keras
import random

from config import *

class AITrain():
    def __init__(self):
        print('Starting Train')
        self.seed_fix()
        self.get_dataset()
        self.reshape_dataset(self.X_train)
        self.reshape_dataset(self.X_test)
        self.get_model()
        self.train()
        
    
    def seed_fix(self, option = 'fix'):
        '''
        Default Option = fix : 42, Available Option = random : 0~1000
        '''
        
        if option == 'fix':
            seed = SeedConfig.fixed_seed
            
        elif option == 'random':
            seed = SeedConfig.random_seed
            
        os.environ['PYTHONHASHSEED'] = str(seed)
        os.environ['TF_DETERMINISTIC_OPS'] = '1'

        random.seed(seed)

        tf.random.set_seed(seed)
        np.random.seed(seed)

        print(f'Seed fixed to {seed}')
        
    def get_dataset(self):
        '''
        root_dir : ex) /home/ai/dataset & to change root_dir fix config.py
        make dataset directory First!!! 
        '''
        root_dir = DatasetConfig.root_dir
        
        categories = np.array(os.listdir(f'{root_dir}/'))
        self.num_classes = len(categories)
        
        print(f'Root DIR : {root_dir} \t Categories : {categories}')
        
        image_w = 224
        image_h = 224
        
        X = []
        Y = []
        
        for idex, category in enumerate(categories):
            label = [0 for i in range(self.num_classes)]
            label[idex] = 1
            print(label)
            image_dir = f'{root_dir}/{category}/'
            
            for top, dir, f in os.walk(image_dir):
                for filename in f:
                    if filename == '.DS_Store' : pass
                    #print(filename)
                    img = cv2.imread(f'{image_dir}{filename}', cv2.IMREAD_COLOR)
                    img = cv2.resize(img, None, fx = image_w / img.shape[1], fy = image_h / img.shape[0])
                    X.append(img)
                    Y.append(label)
                    
        X_train = np.array(X)
        Y_train = np.array(Y)
        
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(X_train, Y_train, test_size=0.2, shuffle=True)
        self.xy = (self.X_train, self.X_test, self.Y_train, self.Y_test)
    
    def reshape_dataset(self, data):
        output_data = data.reshape(data.shape[0], DatasetConfig.reshape('x'), DatasetConfig.reshape('y'), DatasetConfig.reshape('channel'))
        output_data = output_data.astype(DatasetConfig.reshape('astype'))
        output_data /= 255
        
        return output_data
    
    def get_model(self):
        '''
        To use other model change code
        '''
        self.base_model = tf.keras.applications.MobileNet(input_shape=TrainConfig.IMG_SHAPE, include_top=TrainConfig.include_top, weights=TrainConfig.weight, pooling=TrainConfig.polling)
        print(self.base_model.summary())
    
    def ignore_layer_setting(self, ignore_layer):
        for layer in self.base_model.layers[:ignore_layer]:
            layer.trainable = False
        
        for layer in self.base_model.layers[ignore_layer:]:
            layer.trainalbe = True
            
        self.model = tf.keras.Sequential([
            self.base_model
        ])
        
        self.model.add(Dense(self.num_classes, activation = 'softmax'))
           
    def train(self):
        self.ignore_layer_setting(TrainConfig.ignore_layer) # return self.model
        
        self.check_dir()
        
        model_path = f'{TrainConfig.MODEL_SAVE_DIR_PATH}{TrainConfig.model_name}'
        
        cb_chechpoint = ModelCheckpoint(filepath=model_path, monitor=TrainConfig.monitor, verbose=TrainConfig.verbose, save_best_only=TrainConfig.save_best_only)
        
        self.model.compile(loss=TrainConfig.loss, optimizer=TrainConfig.optimizer, metrics=TrainConfig.metrics)
        self.model.fit(self.X_train, self.Y_train, batch_size=TrainConfig.batch_size, epochs=TrainConfig.epochs, callbacks=[cb_chechpoint], validation_data=[self.X_test, self.Y_test])
        
        
    def check_dir(self):
        if not os.path.exists(TrainConfig.MODEL_SAVE_DIR_PATH):
            os.mkdir(TrainConfig.MODEL_SAVE_DIR_PATH)
        
        
AITrain()