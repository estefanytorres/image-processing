# image-processing
Implementation of image processing algorithms inside an "image" class that contains a openCV2 image array

### Image Class contain the following methods

```python
blacknwhite()
```
**Returns:** *image* - A black and white representation of the image


```python
resize_nn(ratio)
```

**Parameters:** **ratio**: desired scale for the new image to apply.

**Returns:** *image* - A copy of the original image with scaled to the passed ratio using nearest neighbor.

```python
resize_pixelreplication(ratio)
```

**Parameters:** **ratio**: desired scale for the new image to apply.

**Returns:** *image* - A copy of the original image with scaled to the passed ratio using pixel replication.

```python
resize_bl(ratio)
```

**Parameters:** **ratio**: desired scale for the new image to apply.

**Returns:** *image* - A copy of the original image with scaled to the passed ratio using bilinear interpolation.

```python
resize_bc(ratio)
```

**Parameters:** **ratio**: desired scale for the new image to apply.

**Returns:** *image* - A copy of the original image with scaled to the passed ratio using bicubic interpolation.

```python
grayScale(levels)
```

**Parameters:** **levels**: desired levels of intensity [2, 256] - *default: 256*

**Returns:** *image* - A copy of the original image with *levels* levels of intensity.

```python
interpolate(ratio, function)
```

**Parameters:** **ratio**: desired scale to interpolate. **function**: type of interpolation ["nn": Nearest neighbor, "bl": Bilinear interpolation, "bc": Bicubic interpolation].


**Returns:** *image* - A copy of the original image that has been rescaled by *ratio* and returned to the original dimentions.

```python
negative()
```

**Returns:** *image* - The negative version of the original image.


```python
save(name)
```

**Parameters:** **name**: desired path and name of the file to save the image.


```python
adjust(x1, y1, x2, y2)
```
This function performs contrast stretching in the image similar to matlab's [imadjust](https://www.mathworks.com/help/images/ref/imadjust.html).

**Parameters:** **x1, y1**: mapping from original image (x1) to desired intensity in new image (y1). **x2, y2**: mapping from original image (x2) to desired intensity in new image (y2).

**Returns:** *image* - A copy of the original image processed by contrast stretching.


