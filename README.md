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

