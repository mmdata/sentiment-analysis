set -e

container_name=movie-review

function print_line () {
   echo "-------------------------------------------------------";
}

function build() {

<<<<<<< HEAD
  if [ ! -e .env ]; then
    echo "[ERROR] File .env is missing, please add it";
    exit 1
  fi

=======
>>>>>>> ed4cd6e4b38882817f02420e67e6b9f8cfb8d369
  # stop if running
  (docker kill $container_name || :) 

  # generate build-info
  python3 ./src/tools/build_info.py

  # clean docker cache
  if promptyn "Force full clean container build (y/n)?"; then
    (docker rmi $container_name || :)
  fi

  # build & run container 
  docker build . -t $container_name 
<<<<<<< HEAD
  # This will read the ./env file and export it's values.
  docker run -d --rm --env-file ./.env -p 8080:8080 --name $container_name $container_name
  echo 
  print_line
  echo "server running on http://localhost:8080/status"
=======
  docker run -d --rm -p 8080:8080 --name $container_name $container_name
  echo 
  print_line
  echo "server running on http://localhost:8080"
>>>>>>> ed4cd6e4b38882817f02420e67e6b9f8cfb8d369
  print_line
}

function promptyn() {
  echo
  while true; do
    read -p "$1 " yn
    case $yn in
    [Yy]*) return 0 ;;
    [Nn]*) return 1 ;;
    *) echo "Please answer yes or no." ;;
    esac
  done
}



function run_install_env () {
   if [ -d test-env ]; then
      echo "test-env found and now activating...";
      source test-env/bin/activate
      # for Windows uncomment below and comment above row
      # source test-env/Scripts/activate
   else
      echo "Warning: test-env NOT found. installing virtualenv and create"
      python3 -m pip install virtualenv
      python3 -m virtualenv test-env
      source test-env/bin/activate
      # for Windows uncomment below and comment above row
      # source test-env/Scripts/activate
      python3 -m pip install -r src/requirements.txt
   fi

   echo "Using python version";
   python3 -c "import sys; print(sys.version)"
}

function run_test(){
  echo "run test"

  # for Windows uncomment below and comment above row
  # source test-env/Scripts/activate
  export PROMETHEUS_USERNAME=user
  export PROMETHEUS_PASSWORD=pass
  #cd optimization-reporting-api
  python3 src/tools/build_info.py
  cd src
   {
    python3 -m pytest -v 
  } || {
    echo "The test failed"
    cd ..
  }
  cd ..
}


# CLI
function run_cli_mode(){
  echo "Running cli manually"
  while true; do
    echo
    docker ps --filter "name=$container_name"
    echo 
    echo "commands:"
    echo "b -> build and start container. If it's the first time you use the shell you should start from here, because you need the build info file. "
    echo "i -> install virtual local environment to run tests" 
    echo "l -> get logs" 
    echo "r -> restart the container" 
    echo "s -> stop container and exit" 
    echo "t -> run unit and functional tests" 
    echo "CRL+C -> quit cli"
    read -p ">>> " action
    case $action in
        b) 
            build
            ;;
        i)
            run_install_env 
            ;;
        l)         
            echo "The logs are:"
            print_line
            (echo 'tail -100 "/log/$(ls /log | grep .json | tail -1)"' | docker exec -i $container_name bash) || :
            print_line
            ;;
        r)      
            echo "restarting server" 
            docker stop $container_name
<<<<<<< HEAD
            docker run -d --rm --env-file ./.env -p 8080:8080 --name $container_name $container_name
=======
            docker run -d --rm -p 8080:8080 --name $container_name $container_name
>>>>>>> ed4cd6e4b38882817f02420e67e6b9f8cfb8d369
            echo "done ..."
            ;;
        s)      
            echo "exit server" 
            (docker kill $container_name || :)
            echo "done ..."
            exit 0
            ;;
        t)      
            run_test
            ;;
      *)
            ;;
    esac
  done
}

case $1 in         
   * )
               run_cli_mode;
               ;;
esac
