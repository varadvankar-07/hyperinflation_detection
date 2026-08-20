.. code:: ipython3

    can = "soda"
    can




.. parsed-literal::

    'soda'



.. code:: ipython3

    can = "beans"
    can




.. parsed-literal::

    'beans'



.. code:: ipython3

    type(pizza)




.. parsed-literal::

    int



.. code:: ipython3

    pizza=100
    pizza




.. parsed-literal::

    100



.. code:: ipython3

    samosa=50
    pav_vada=20.5
    pav_vada




.. parsed-literal::

    20.5



.. code:: ipython3

    total = pizza + samosa + pav_vada
    total




.. parsed-literal::

    170.5



.. code:: ipython3

    total > 100




.. parsed-literal::

    True



.. code:: ipython3

    type(total)




.. parsed-literal::

    float



.. code:: ipython3

    above_thresold = total > 200
    above_thresold




.. parsed-literal::

    False



.. code:: ipython3

    can  = "food"
    can




.. parsed-literal::

    'food'



.. code:: ipython3

    can




.. parsed-literal::

    'food'



.. code:: ipython3

    type(can)




.. parsed-literal::

    str



.. code:: ipython3

    food = "jalebi"
    food




.. parsed-literal::

    'jalebi'



.. code:: ipython3

    bar=food
    bar




.. parsed-literal::

    'jalebi'



.. code:: ipython3

    id(bar)




.. parsed-literal::

    2315417185728



.. code:: ipython3

    id(food)




.. parsed-literal::

    2315436767920



.. code:: ipython3

    bar = "samosa"
    bar




.. parsed-literal::

    'samosa'



.. code:: ipython3

    id(bar)




.. parsed-literal::

    2315417185728



.. code:: ipython3

    def = "hello"


::


      Cell In[58], line 1
        def = "hello"
            ^
    SyntaxError: invalid syntax
    


.. code:: ipython3

    name_person='varad'
    name_person




.. parsed-literal::

    'varad'



.. code:: ipython3

    base = 20.5
    height = 20
    area = 1/2 * base * height 
    area




.. parsed-literal::

    205.0



.. code:: ipython3

    type(area)




.. parsed-literal::

    float



.. code:: ipython3

    foo = "jalebi"
    foo




.. parsed-literal::

    'jalebi'



.. code:: ipython3

    bar=foo 
    bar




.. parsed-literal::

    'jalebi'



.. code:: ipython3

    id(bar)




.. parsed-literal::

    2315436767920



.. code:: ipython3

    print(id(foo))


::


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[6], line 1
    ----> 1 print(id(foo))
    

    NameError: name 'foo' is not defined

