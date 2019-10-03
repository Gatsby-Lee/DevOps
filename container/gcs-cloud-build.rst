Cloud Build
===========


Task 2. Building Containers with DockerFile and Cloud Build
-----------------------------------------------------------

quickstart.sh

#!/bin/sh
echo "Hello, world! The time is $(date)."

Dockerfile

FROM alpine
COPY quickstart.sh /
CMD ["/quickstart.sh"]

chmod +x quickstart.sh

gcloud builds submit --tag gcr.io/${GOOGLE_CLOUD_PROJECT}/quickstart-image .


Task 3. Building Containers with a build configuration file and Cloud Build
---------------------------------------------------------------------------


$ git clone https://github.com/GoogleCloudPlatformTraining/training-data-analyst

cd ~/training-data-analyst/courses/ak8s/02_Cloud_Build/a

$ ls -al
total 20
drwxr-xr-x 2 google5476553_student google5476553_student 4096 Oct  3 08:43 .
drwxr-xr-x 4 google5476553_student google5476553_student 4096 Oct  3 08:43 ..
-rw-r--r-- 1 google5476553_student google5476553_student  164 Oct  3 08:43 cloudbuild.yaml
-rw-r--r-- 1 google5476553_student google5476553_student   56 Oct  3 08:43 Dockerfile
-rw-r--r-- 1 google5476553_student google5476553_student   53 Oct  3 08:43 quickstart.sh

This file instructs Cloud Build to use Docker to build an image using the Dockerfile specification
in the current local directory, tag it with gcr.io/$PROJECT_ID/quickstart-image
($PROJECT_ID is a substitution variable automatically populated by Cloud Build with the project ID of the associated project)
and then push that image to Container Registry.

$ cat cloudbuild.yaml
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: [ 'build', '-t', 'gcr.io/$PROJECT_ID/quickstart-image', '.' ]
images:
- 'gcr.io/$PROJECT_ID/quickstart-image'

$ cat Dockerfile
FROM alpine
COPY quickstart.sh /
CMD ["/quickstart.sh"]

$ cat quickstart.sh
#!/bin/sh
echo "Hello, world! The time is $(date)."

gcloud builds submit --config cloudbuild.yaml .

$ gcloud builds submit --config cloudbuild.yaml .
Creating temporary tarball archive of 3 file(s) totalling 273 bytes before compression.
Uploading tarball of [.] to [gs://qwiklabs-gcp-b8f54de83b220f42_cloudbuild/source/1570117672.67-ac46a759574243589c8b374ad6b2be1b.tgz]
Created [https://cloudbuild.googleapis.com/v1/projects/qwiklabs-gcp-b8f54de83b220f42/builds/6ae976c1-fcd0-4863-b817-33cf405a7240].
Logs are available at [https://console.cloud.google.com/gcr/builds/6ae976c1-fcd0-4863-b817-33cf405a7240?project=947440574606].
------------------------------------------------------------------ REMOTE BUILD OUTPUT -------------------------------------------------------------------
starting build "6ae976c1-fcd0-4863-b817-33cf405a7240"

FETCHSOURCE
Fetching storage object: gs://qwiklabs-gcp-b8f54de83b220f42_cloudbuild/source/1570117672.67-ac46a759574243589c8b374ad6b2be1b.tgz#1570117673270439
Copying gs://qwiklabs-gcp-b8f54de83b220f42_cloudbuild/source/1570117672.67-ac46a759574243589c8b374ad6b2be1b.tgz#1570117673270439...
/ [1 files][  375.0 B/  375.0 B]
Operation completed over 1 objects/375.0 B.
BUILD
Already have image (with digest): gcr.io/cloud-builders/docker
Sending build context to Docker daemon  4.096kB
Step 1/3 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:acd3ca9941a85e8ed16515bfc5328e4e2f8c128caa72959a58a127b7801ee01f
Status: Downloaded newer image for alpine:latest
 ---> 961769676411
Step 2/3 : COPY quickstart.sh /
 ---> 0220b49e008f
Step 3/3 : CMD ["/quickstart.sh"]
 ---> Running in 1ff1d0056818
Removing intermediate container 1ff1d0056818
 ---> 092dfbd2de50
Successfully built 092dfbd2de50
Successfully tagged gcr.io/qwiklabs-gcp-b8f54de83b220f42/quickstart-image:latest
PUSH
Pushing gcr.io/qwiklabs-gcp-b8f54de83b220f42/quickstart-image
The push refers to repository [gcr.io/qwiklabs-gcp-b8f54de83b220f42/quickstart-image]
c2d1a8d8dd6e: Preparing
03901b4a2ea8: Preparing
03901b4a2ea8: Layer already exists
c2d1a8d8dd6e: Pushed
latest: digest: sha256:21e6489f75eb4b022b79529fd467634dbb0d4da43772c0b51837a5299579a2a6 size: 735
DONE
----------------------------------------------------------------------------------------------------------------------------------------------------------

ID                                    CREATE_TIME                DURATION  SOURCE                          IMAGES                                                           STATUS
6ae976c1-fcd0-4863-b817-33cf405a7240  2019-10-03T15:47:53+00:00  13S       gs://qwiklabs-gcp-b8f54de83b220f42_cloudbuild/source/1570117672.67-ac46a759574243589c8b374ad6b2be1b.tgz  gcr.io/qwiklabs-gcp-b8f54de83b220f42/quickstart-image (+1 more)  SUCCESS




Task 4. Building and Testing Containers with a build configuration file and Cloud Build
---------------------------------------------------------------------------------------

cd ~/training-data-analyst/courses/ak8s/02_Cloud_Build/b

google5476553_student@cloudshell:~/training-data-analyst/courses/ak8s/02_Cloud_Build/b (qwiklabs-gcp-b8f54de83b220f42)$ cat cloudbuild.yaml
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: [ 'build', '-t', 'gcr.io/$PROJECT_ID/quickstart-image', '.' ]
- name: 'gcr.io/$PROJECT_ID/quickstart-image'
  args: ['fail']
images:
- 'gcr.io/$PROJECT_ID/quickstart-image'

In addition to its previous actions, this build configuration file runs the quickstart-image it has created. In this task, the quickstart.sh script has been modified so that it simulates a test failure when an argument ['fail'] is passed to it.


google5476553_student@cloudshell:~/training-data-analyst/courses/ak8s/02_Cloud_Build/b (qwiklabs-gcp-b8f54de83b220f42)$ cat Dockerfile
FROM alpine
COPY quickstart.sh /
CMD ["/quickstart.sh"]
google5476553_student@cloudshell:~/training-data-analyst/courses/ak8s/02_Cloud_Build/b (qwiklabs-gcp-b8f54de83b220f42)$ cat quickstart.sh
#!/bin/sh
if [ -z "$1" ]
then
        echo "Hello, world! The time is $(date)."
        exit 0
else
        exit 1
fi


$ gcloud builds submit --config clou
dbuild.yaml .
Creating temporary tarball archive of 3 file(s) totalling 382 bytes before compression.
Uploading tarball of [.] to [gs://qwiklabs-gcp-b8f54de83b220f42_cloudbuild/source/1570118108.22-4b36de0b571e4e898302be2dcf72ea38.tgz]
Created [https://cloudbuild.googleapis.com/v1/projects/qwiklabs-gcp-b8f54de83b220f42/builds/920137b3-f605-432d-be7b-2ea9df004758].
Logs are available at [https://console.cloud.google.com/gcr/builds/920137b3-f605-432d-be7b-2ea9df004758?project=947440574606].
------------------------------------------------------------------ REMOTE BUILD OUTPUT -------------------------------------------------------------------
starting build "920137b3-f605-432d-be7b-2ea9df004758"
FETCHSOURCE
Fetching storage object: gs://qwiklabs-gcp-b8f54de83b220f42_cloudbuild/source/1570118108.22-4b36de0b571e4e898302be2dcf72ea38.tgz#1570118108813049
Copying gs://qwiklabs-gcp-b8f54de83b220f42_cloudbuild/source/1570118108.22-4b36de0b571e4e898302be2dcf72ea38.tgz#1570118108813049...
/ [1 files][  418.0 B/  418.0 B]
Operation completed over 1 objects/418.0 B.
BUILD
Starting Step #0
Step #0: Already have image (with digest): gcr.io/cloud-builders/docker
Step #0: Sending build context to Docker daemon  4.096kB
Step #0: Step 1/3 : FROM alpine
Step #0: latest: Pulling from library/alpine
Step #0: Digest: sha256:acd3ca9941a85e8ed16515bfc5328e4e2f8c128caa72959a58a127b7801ee01f
Step #0: Status: Downloaded newer image for alpine:latest
Step #0:  ---> 961769676411
Step #0: Step 2/3 : COPY quickstart.sh /
Step #0:  ---> 66c65434c444
Step #0: Step 3/3 : CMD ["/quickstart.sh"]
Step #0:  ---> Running in cde6b21b3071
Step #0: Removing intermediate container cde6b21b3071
Step #0:  ---> ea1310994697
Step #0: Successfully built ea1310994697
Step #0: Successfully tagged gcr.io/qwiklabs-gcp-b8f54de83b220f42/quickstart-image:latest
Finished Step #0
Starting Step #1
Step #1: Already have image: gcr.io/qwiklabs-gcp-b8f54de83b220f42/quickstart-image
Step #1: docker: Error response from daemon: OCI runtime create failed: container_linux.go:345: starting container process caused "exec: \"fail\": executa
ble file not found in $PATH": unknown.
Step #1: time="2019-10-03T15:55:21Z" level=error msg="error waiting for container: context canceled"
Finished Step #1
ERROR
ERROR: build step 1 "gcr.io/qwiklabs-gcp-b8f54de83b220f42/quickstart-image" failed: exit status 127
----------------------------------------------------------------------------------------------------------------------------------------------------------
ERROR: (gcloud.builds.submit) build 920137b3-f605-432d-be7b-2ea9df004758 completed with status "FAILURE"
