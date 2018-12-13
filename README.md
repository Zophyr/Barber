# Barber

✂️ Cut the string with blank and line break. 

## What is Barber? 

**before** 👇 

```shell
e36bc283b3ae643d85ba28ae12d09f61b48dd3e9f7f816ad692d60de96d0df59dbc3ace23348ab1a6a1dcd0e9840b733
```

**after** 👇 

```shell
e36b c283 b3ae 643d 85ba 28ae 12d0 9f61
b48d d3e9 f7f8 16ad 692d 60de 96d0 df59
dbc3 ace2 3348 ab1a 6a1d cd0e 9840 b733
```

## How to cut?

**Sample Usage**

```python
>>> from barber import barber
>>> 
>>> str = "e36bc283b3ae643d85ba28ae12d09f61b48dd3e9f7f816ad692d60de96d0df59dbc3ace23348ab1a6a1dcd0e9840b733"
>>>
>>> barber.cut(str)
'e36b c283 b3ae 643d 85ba 28ae 12d0 9f61 \nb48d d3e9 f7f8 16ad 692d 60de 96d0 df59 \ndbc3 ace2 3348 ab1a 6a1d cd0e 9840 b733 \n'
```

## How to cut more pretty? 

```python
cut(str, length, group, style)
```

- **str** is the string waiting for the haircut.

- **length** is how many chars to cut once.
    - default is 4

- **group** is how many group to line break.
    - default is 8

- **style** is the symbol of the interval between each group
    - default is blank

**demo**

```python
>>> barber.cut(str, 3, 10, "%")
'e36%bc2%83b%3ae%643%d85%ba2%8ae%12d%09f%\n61b%48d%d3e%9f7%f81%6ad%692%d60%de9%6d0%\ndf5%9db%c3a%ce2%334%8ab%1a6%a1d%cd0%e98%\n40b%733%'
```

It will be like this: 

```shell
e36%bc2%83b%3ae%643%d85%ba2%8ae%12d%09f%
61b%48d%d3e%9f7%f81%6ad%692%d60%de9%6d0%
df5%9db%c3a%ce2%334%8ab%1a6%a1d%cd0%e98%
40b%733%
```
