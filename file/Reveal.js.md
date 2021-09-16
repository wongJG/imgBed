

## Reveal.js

Reveal.js is an open-sourced js project by [Hakim El Hattab](http://hakim.se/) that helps you design presentation slides in no time. See detail [installation guide](https://revealjs.com/installation/).



## Getting started



### A basic slide

You can create a simple slide just by,

```html
<section>
  <h2>Testing presentation</h2>
  <p>
    <small>Author Name</small>
  </p>
</section>
```



### Utilising Markdown technique

Add the `data-markdown` attribute to your `<section>` element 

```html
<section data-markdown>
  <textarea data-template>
    ## Slide 1
    A paragraph with some text and a [link](http://hakim.se).
    ---
    ## Slide 2
    <!--Unorder list -->
    * A
	  * B
	  * C
    ---
    ## Slide 3
    <!--Inserting images in Markdown grammar -->
    ![arrow.png](https://static.slid.es/reveal/arrow.png)
  </textarea>
</section>
```

Also, step to step syntax highlighting is supported.

~~~html
<section data-markdown>
  <textarea data-template>
    ```js [1-2|3|4] <!--Prodce 3 slides, highlighting different lines-->
    let a = 1; 
    let b = 2;
    let c = x => 1 + 2 + x;
    c(3);
    ```
  </textarea>
</section> 
~~~

