class DatasetConfig():
    TASK = 'sign'
    CATEGORIES = ['like', 'dislike', 'stop']

    import random
from datetime import datetime
import tensorflow as tf
import os

class SeedConfig():
    fixed_seed = 42
    random_seed = random.randint(0, 1000)
    
class DatasetConfig():
    root_dir = 'dataset/train'
    
    def reshape(option):
        '''
        option list(x, y, channel, astype)
        x = 224
        y = 224
        channel = 3
        astype = float32
        '''
        if option == 'x': return 224
        elif option == 'y' : return 224
        elif option == 'channel' : return 3
        elif option == 'astype' : return 'float32'
        
class TrainConfig():
    IMG_SIZE = 224
    IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 3)
    include_top = False
    weight = 'imagenet'
    polling = 'max'
    
    ignore_layer = 24
    
    MODEL_SAVE_DIR_PATH = 'model/'
    model_name = f'{datetime.now().strftime("%Y%m%d%H%M")}.h5'
    
    monitor = 'val_accuracy'
    verbose = 1
    save_best_only = True
    
    loss = 'binary_crossentropy'
    lr = 0.0001
    optimizer = tf.keras.optimizers.legacy.Adam(learning_rate= lr)
    metrics = ['accuracy']
    
    batch_size = 50
    epochs = 10
    
class TestConfig():
    root_dir = 'dataset/test'

    test_dir = 'test/'
    ex = '.jpg'
    
    IMG_SIZE = 224
    IMG_SHAPE = (IMG_SIZE, IMG_SIZE, 3)
    
    model = 'model/best_model.h5'
    
    def reshape(option):
        '''
        option list(x, y, channel, astype)
        defalut x = 224
        defalut y = 224
        defalut channel = 3
        defalut astype = float32
        '''
        if option == 'x': return 224
        elif option == 'y' : return 224
        elif option == 'channel' : return 3
        elif option == 'astype' : return 'float32'
        
    classes = os.listdir(f'{root_dir}/')