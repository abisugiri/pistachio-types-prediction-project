
# Pistachio types detection

There are several types of pisctachio in the world and this project is focusing on predicting two types, these are "Kirmizi_Pistachio" and "Siit_Pistachio". The main objective of this project is to help customers and retailers in classifying based on dataset of the pistachio's physical characteristics.



## Dataset Overview

| Column | Description |
| --- | --- |
| `AREA` | The area of the pistachio region detected in the image |
| `PERIMETER` | The perimeter (total length) of the pistachio region boundary |
| `MAJOR_AXIS` | The length of the major axis of the ellipse that best fits the pistachio region|
| `MINOR_AXIS` | The length of the minor axis of the ellipse that best fits the pistachio region |
| `ECCENTRICITY` | The eccentricity of the ellipse that describes the elongation of the pistachio region |
| `EQDIASQ` | The equivalent diameter of the pistachio region |
| `SOLIDITY` | The ratio of the pistachio region's area to the area of its convex hull |
| `CONVEX_AREA` | The area of the convex hull of the pistachio region |
| `EXTENT` | The ratio of the area of the pistachio region to the area of the bounding box that encloses it |
| `ASPECT_RATIO` | The ratio of the major axis length to the minor axis length, indicating the shape of the pistachio region |
| `ROUNDNESS` | A measure of how closely the pistachio region resembles a perfect circle (circularity) |
| `COMPACTNESS` | A measure of how compact the shape of the pistachio region is |
| `SHAPEFACTOR_1` | Shape factor 1, a geometric descriptor calculated from the area and perimeter of the pistachio region |
| `SHAPEFACTOR_2` | Shape factor 2, another geometric descriptor calculated from the area and perimeter of the pistachio region |
| `SHAPEFACTOR_3` | Shape factor 3, a geometric descriptor derived from the area and perimeter of the pistachio region |
| `SHAPEFACTOR_4` | Shape factor 4, another geometric descriptor derived from the area and perimeter of the pistachio region |
| `y` | The class or category of the pistachio |


## Dataset Source

[Pistachio types detection](https://www.kaggle.com/datasets/amirhosseinmirzaie/pistachio-types-detection)
## Author

- Abi Rahman Sugiri [@abisugiri](https://www.github.com/abisugiri)


## Deployment

To deploy this project run

```bash
  https://huggingface.co/spaces/abisugiri/pistachio-types-prediction
```

