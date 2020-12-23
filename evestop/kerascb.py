from keras.callbacks import Callback
from evestop.generic as g

class EVEEarlyStopping(Callback):
  def __init__(self,
               monitor='val_loss',
               min_delta=0,
               patience=0,
               verbose=0,
               mode='min',
               baseline=0,
               restore_best_weights=False):
    super(EarlyStopping, self).__init__()

    self.eve = g.EVEEarlyStopping(patience=patience,
                                  mode=mode,
                                  min_delta=min_delta,
                                  baseline=baseline)

  def on_train_begin(self, logs=None):
    self.eve.reset()

  def on_epoch_end(self, epoch, logs=None):
    current = self.get_monitor_value(logs)
    
    if current is None:
      return

    self.eve.register(current, self.model.get_weights())

    if not self.eve.proceed:
        if self.restore_best_weights:
            if self.verbose > 0:
            print('Restoring model weights from the end of the best epoch.')
            self.model.set_weights(self.eve.best_measuree)

  def on_train_end(self, logs=None):
    if self.stopped_epoch > 0 and self.verbose > 0:
      print('Epoch %05d: early stopping' % (self.stopped_epoch + 1))

  def get_monitor_value(self, logs):
    logs = logs or {}
    monitor_value = logs.get(self.monitor)
    if monitor_value is None:
      logging.warning('Early stopping conditioned on metric `%s` '
                      'which is not available. Available metrics are: %s',
                      self.monitor, ','.join(list(logs.keys())))
    return monitor_value