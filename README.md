# python_works

Example python programs

## Environments

### Create

```sh
conda create -n envname python=3.13

conda create --name envname --file envname.yml
```

### Remove

```sh
conda remove -n envname

conda remove --name envname
```

### Export

```sh
conda export
conda export --file FILE_NAME
conda export --format yaml
conda export --file environment.yaml
```

### List

```sh
conda env list

conda info --envs
```

### Info

```sh
conda info
```
