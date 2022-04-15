FROM tensorflow/tensorflow:devel

WORKDIR /tensorflow_src

RUN git pull

RUN apt-get update
RUN apt-get install -y unzip graphviz

RUN pip install --upgrade pip

RUN ./configure
RUN bazel build --config=opt --jobs 1 --local_ram_resources 2048 --local_cpu_resources 2 --verbose_failures //tensorflow/tools/pip_package:build_pip_package
RUN ./bazel-bin/tensorflow/tools/pip_package/build_pip_package /mnt
RUN chown $HOST_PERMS /mnt/tensorflow-version-tags.whl

RUN pip uninstall tensorflow
RUN pip install /mnt/tensorflow-2.8.0
RUN cd /tmp


# RUN useradd -m gdl
# ENV PATH="/home/gdl/.local/bin:${PATH}"

# WORKDIR /app

# RUN chown -R gdl:gdl /app

# USER gdl

# COPY ./requirements.txt /app
# RUN pip install --user -r /app/requirements.txt

# COPY /models/. /app/models
# COPY /utils/. /app/utils
# COPY /notebooks/. /app/notebooks
# COPY /scripts/. /app/scripts

# COPY /setup.cfg /app

# ENV PYTHONPATH="${PYTHONPATH}:/app"