# Fashion-recommended-system

 In this project, we proposed a personalized Fashion Recommender system that generates recommendations for the user based on an input given.
 Unlike the conventional systems that rely on the user's previous purchases and history, this project aims at using an image of a product given as 
 input by the user to generate recommendations since many-a-time people see something that they are interested in and tend to look for products that
 are similar to that. We use neural networks to process the images from Fashion Product Images Dataset and the Nearest neighbour backed recommender to
 generate the final recommendations.<br>
 
 Link to the dataset:-https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small
 
 ## Training the neural networks

Once the data is pre-processed, the neural networks are trained, utilizing transfer learning from ResNet50. More additional layers are added in the last layers that replace the architecture and weights from ResNet50 in order to fine-tune the network model to serve the current issue. The figure shows the ResNet50 architecture.

![resnet](https://user-images.githubusercontent.com/68815179/199084513-80b644fc-3adc-4b20-b553-8e2e1ba81538.png)

## Recommendation generation

- To generate recommendations, our proposed approach uses Sklearn Nearest neighbours(KNN). This allows us to find the nearest neighbours for the given input image. The top 6 recommendations are extracted from the database and their images are displayed.
- The concept of Transfer learning is used to overcome the issues of the small size Fashion dataset. Therefore we pre-train the classification models on the DeepFashion dataset that consists of 44,441 garment images. 
- The networks are trained and validated on the dataset taken. The training results show a great accuracy of the model with low error, loss and good f-score.

## Screenshots

![image](https://user-images.githubusercontent.com/68815179/199086633-e52519b8-bb29-458d-9b16-71da9937bacd.png)

Different outfits generated for the given input image

![image](https://user-images.githubusercontent.com/68815179/199087048-1c5d857e-8aae-4a13-97db-33ea674e94a7.png)

![image](https://user-images.githubusercontent.com/68815179/199087165-a1c0e16b-a787-4a46-95aa-31ae39e66110.png)

![image](https://user-images.githubusercontent.com/68815179/199087374-f4f2c861-1bcf-4164-ad1c-d91b23131e98.png)

![image](https://user-images.githubusercontent.com/68815179/199087493-d147d80a-0939-43a1-a867-f9b8f5738ac3.png)
