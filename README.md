# StreamlitFastAPI

Simple example of usage of streamlit and FastAPI for ML model serving.

- Create a basic Python Calculator module. 
- Serve the function from the module using FastAPI. 
- Creating a very basic UI using Streamlit. 
- Integrating Streamlit &amp; FastAPI.

To run the example in a machine running Docker and docker-compose, run:

    docker-compose build
    docker-compose up

To visit the FastAPI documentation of the resulting service, visit http://localhost:8500 with a web browser.  
To visit the streamlit UI, visit http://localhost:8501.

Logs can be inspected via:

    docker-compose logs

## Deployment

To deploy the app, one option is deployment on Heroku (with [Dockhero](https://elements.heroku.com/addons/dockhero)). To do so:

- rename `docker-compose.yml` to `dockhero-compose.yml`
- create an app (we refer to its name as `<my-app>`) on a Heroku account
- install locally the Heroku CLI, and enable the Dockhero plugin with `heroku plugins:install dockhero`
- add to the app the DockHero add-on (and with a plan allowing enough RAM to run the model!)
- in a command line enter `heroku dh:compose up -d --app <my-app>` to deploy the app
- to find the address of the app on the web, enter `heroku dh:open --app <my-app>`
- to visualize the api, visit the address adding port `8500/docs`, e.g. `http://dockhero-<named-assigned-to-my-app>-12345.dockhero.io:8500/docs`(not `https`)
- visit the address adding `:8501` to visit the streamlit interface
- logs are accessible via `heroku logs -p dockhero --app <my-app>`

