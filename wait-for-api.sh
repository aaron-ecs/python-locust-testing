#!/usr/bin/env bash
echo "Waiting for user exercises rest API to start..."

attempt_counter=0
max_attempts=12

until $(curl --output /dev/null --silent --head --fail http://api:8080); do
    if [[ ${attempt_counter} -eq ${max_attempts} ]];then
      echo "user exercises rest cannot API reached!"
      exit 1
    fi

    printf '.'
    attempt_counter=$(($attempt_counter+1))
    sleep 5
done

echo "user exercises rest API has been reached!"

locust --host=http://api:8080 --no-web -c 1000 -r 20 --run-time 1m