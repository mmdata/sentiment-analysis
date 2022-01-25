# sentiment-analysis

## About this Application
<<<<<<< HEAD
This application implements different Machine Learning models to predict the sentiment of a sentence.
The training data used are the IMDB Movie Review dataset.

### Use the CLI
For common usecases and scripts there is a command line interface (CLI) tool. Notice that the cli assume that you're running on a UNIX based machine. If you're using Windows you will have to change some command (There are comments in the cli.sh file that explain what you should change)
The application will also need a `.env` file like this in the root of the project:
``` 
ENV_VARIABLE_EXAMPLE=222
```
This is just to showcase how we can read env variables in docker container. You can verify that it's correctly reading the file when you call the `status` endpoint
=======
This application implements a simple Machine Learning models to predict the sentiment of a sentence.
The training data used are the IMDB Movie Review dataset.

### To Do
- Initialise logger and log messages whenever we train the model or we predict. Maybe reuse the one in config.py
- write integration tests
- add gitHub Action



### Use the CLI
For common usecases and scripts there is a command line interface (CLI) tool. Notice that the cli assume that you're running on a UNIX based machine. If you're using Windows you will have to change some command (There are comments in the cli.sh file that explain what you should change)
>>>>>>> ed4cd6e4b38882817f02420e67e6b9f8cfb8d369

To start the cli:

```bash
./cli.sh
```
To build and run the container you can select `b`.
To check thath the application is running visit `http://localhost:8080/status`

### Run unit and functional tests with pytest

To run the tests:
- start cli with `./cli.sh`
- Type `i` to create/activate a virtual environment
- Type `t` 

## Linux Know-How
To see the write/read permission of a file:
- `ls -l`
To set a file s.t everyone can read and write it https://phoenixnap.com/kb/linux-file-permissions:
- `chmod u=rwx,g=rwx,o=rwx file_name`
or:
- `chmod +x filename`
