# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### docker run -it -p 8080:8080 app1-docker
to start the back-end run in a docker container

and then to start the front-end of the application

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)




###############################################################
Push your container image to a registry

Following the next url, https://azure.github.io/AppService/2021/03/04/How-to-Host-a-Python-application-with-Windows-Containers-on-App-Service.html



Now that we’ve tested the application locally in a container we can push it to a container registry where the image will live. This will prepare us and satisfy the requirements for creating and publishing the application to App Service. First you must have a registry created before you can push the image to it. Once that is complete, you can continue with these instructions. For this example, we will be using Azure Container Registry, but you can use Docker Hub as well by swapping out the registry-name.azurecr.io with your-docker-hub-registry-name.

Before you attempt to tag and push the image, make sure you are logged in by using docker login in the command prompt

docker login <registry-name>.azurecr.io
This will prompt you to enter your username and password from your registry. You can find these under Access keys in your Container registry resource in the Azure portal.

After you’ve logged in, run the following commands to tag and push your Docker image:

docker tag mypythonapp:latest <registry-name>.azurecr.io/mypythonapp:latest
docker push <registry-name>.azurecr.io/mypythonapp:latest
Once the image is pushed you can verify that it is in your Azure Container Registry by viewing the Repositories in your Container registry resource. Next, we will use the image from our registry to create our Web App on App Service.

Create the Web App using Premium v3
When you are creating the Web App that you will publish your container to be sure to choose the correct options shown below. Name your site, choose Docker Container under Publishing type and Windows for the Operating System. Choose an available Region and then choose your SKU and size. Premium V3 is the only SKU that supports Windows containers. Learn more about the Premium V3 SKU here.

Azure Web App

Next, click the Next:Docker > button to pull your container image from Azure Container Registry.

Choose Azure Container Registry as your Image Source and the registry options will show up for you to select. The registry you selected earlier should show up in the Registry drop-down along with the created Images and Tags.

Azure Web App

Once you have the correct options selected you can hit Review + create to start your deployment and verify your deployed app on App Service.