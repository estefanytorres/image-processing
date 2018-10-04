# image-processing
Implementation of image processing algorithms inside an "image" class that contains a openCV2 image array

### Image Class contain the following methods

```python
blacknwhite():
```
**Returns:** *image* - A black and white representation of the image


```python
resize_nn(ratio):
```

**Parameters:** **ratio**: desired scale for the new image to apply.

**Returns:** *image* - A copy of the original image with scaled to the passed ratio using nearest neighbor.

```python
resize_pixelreplication(ratio):
```

**Parameters:** **ratio**: desired scale for the new image to apply.

**Returns:** *image* - A copy of the original image with scaled to the passed ratio using pixel replication.

```python
resize_bl(ratio):
```

**Parameters:** **ratio**: desired scale for the new image to apply.

**Returns:** *image* - A copy of the original image with scaled to the passed ratio using bilinear interpolation.

```python
resize_bc(ratio):
```

**Parameters:** **ratio**: desired scale for the new image to apply.

**Returns:** *image* - A copy of the original image with scaled to the passed ratio using bicubic interpolation.
