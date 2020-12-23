class EVEEarlyStopping():
    proceed = True

    def reset(self):
        self.smoothed_quality = self.baseline
        self.best_smoothed_quality = self.smoothed_quality
        self.iters_since_record = 0
        self.best_measuree = None

    def __init__(self, baseline=0, 
                       patience=1000, 
                       smoothing=0.75,
                       min_delta=0, 
                       mode='max'):
        self.patience = patience
        self.smoothing = smoothing
        self.baseline = baseline
        self.min_delta = min_delta

        if mode == 'max':
            self.minimize = False
        elif mode == 'min':
            self.minimize = True
        else:
            raise ValueError('Unsupported mode. Choose min or max')

        self.reset()

    def register(self, measurement, measuree=None):
        self.iters_since_record += 1

        quality = -measurement if self.minimize else measurement
        quality -= self.min_delta
        self.smoothed_quality = self.smoothed_quality * self.smoothing + quality * (1 - self.smoothing)

        if self.smoothed_quality > self.best_smoothed_quality:
            self.best_smoothed_quality = self.smoothed_quality
            self.best_measuree = measuree
            self.iters_since_record = 0

        self.proceed = self.iters_since_record <= self.patience