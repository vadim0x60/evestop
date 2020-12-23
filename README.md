# Exponential Variance Elimination

A better early stopping strategy for iterative optimization problems like, say, training deep neural networks.

## How early stopping usually works

```
while iters_since_record <= patience:
    optimize_step()
    quality = measure_quality()

    if quality > best_quality:
        best_quality = quality
        iters_since_record = 0
```

This method has an important failure mode: 
1. Early in the optimization process one unusually good (but far from optimal) result is obtained due to a fortunate coincidence.
2. The optimization continues for `patience` steps, but the outlier isn't superceded.
3. The training is stopped early, because of one outlier and despite a clear positive trend.

## How EVE works

```
while iters_since_record <= patience:
    optimize_step()
    quality = measure_quality()
    smoothed_quality = smoothed_quality * smoothing + quality * (1 - smoothing)

    if smoothed_quality > best_smoothed_quality:
        best_smoothed_quality = smoothed_quality
        iters_since_record = 0
```

This early stopping method tracks the exponential moving average of the variable instead of the variable itself, thus the training is stopped when positive *trend* stops.


## How to use this package

Start with

```
pip install evestop
```

If you're using keras, just replace `tf.keras.callbacks.EarlyStopping` callback with our `evestop.kerascb.EarlyStopping` 

If you're writing the optimization loop yourself, create the early stopping rule (make sure to set mode to 'min' if the vairable is being minimised):

```
from evestop.generic import EveEarlyStopping
eve = EveEarlyStopping(baseline=0, patience=1000, moothing=0.75, min_delta=0, mode='max')
```

And start optimizing your favourite variable with your favourite optimization algorithm.
At every iteration you should call `eve.register(measurement)`, then check `eve.proceed` attribute. If early stopping is called for, it will be `False`.
See `examples` for more information.