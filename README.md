## Pascal Triangle
### The repo description

This repository was created to explore the Pascal Triangle.

### The problems

1. We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:
```
       1       
      1 1      
     1 2 1     
    1 3 3 1    
   1 4 6 4 1   
 1 5 10 10 5 1 
1 6 15 20 15 6 1
```

However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are
not divisible by 7. Find the number of entries which are not divisible by 7 in the first one billion 
(10<sup>9</sup>) rows of Pascal'striangle.

### The solution

For the theory of the solution please check 
[this document][Theory].

The solution of the problem is implemented in the current app.

Also for clarity there were implemented functions to display Pascal's triangle and Sierpinski's triangle.

### Requirements

To build this project you will need [Docker][Docker Install].

Or you can use virtual environment.

### Installation
```bash
$ git clone https://github.com/DenisMaley/pascal-triangle.git
```
```bash
$ cd pascal-triangle
```
```bash
$ make install
```

If you face issues try docker command directly:

```bash
$ docker build -t pascal-triangle .
```

If you want to use venv:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Usage

1. To display Pascal's triangle:
```bash
$ make pascal-triangle NUM=5
```
where `NUM` is the number of rows

Alternatives: 

Docker command:

```bash
$ docker run --rm -it pascal-triangle pascal-triangle -n 5
```

Venv:

```bash
$ python app.py pascal-triangle -n 5
```

2. To display Sierpinski's triangle:
```bash
$ make sierpinski-triangle NUM=100 DIVIDER=7
```
where `NUM` is the number of rows

Alternatives: 

Docker command:

```bash
$ docker run --rm -it pascal-triangle sierpinski-triangle -n 100 -d 7
```

Venv:

```bash
$ python app.py sierpinski-triangle -n 100 -d 7
```

3. To find the number of entries which are not divisible by 
a prime number in the first n rows of Pascal'striangle:
```bash
$ make not-div-count NUM=1000000000 DIVIDER=7
```
where `NUM` is the number of rows, `DIVIDER` is the prime number.

Alternatives: 

Docker command:

```bash
$ docker run --rm -it pascal-triangle not-div-count -n 1000000000 -d 7
```

Venv:

```bash
$ python app.py not-div-count -n 1000000000 -d 7
```

### Examples

1. Display Pascal's Triangle

```bash
$ make pascal-triangle NUM=10
```

```
             1             
            1 1            
           1 2 1           
          1 3 3 1          
         1 4 6 4 1         
       1 5 10 10 5 1       
     1 6 15 20 15 6 1     
    1 7 21 35 35 21 7 1    
  1 8 28 56 70 56 28 8 1  
1 9 36 84 126 126 84 36 9 1
```
2. Display Sierpinski Triangle

```bash
$ make sierpinski-triangle NUM=32 DIVIDER=2
```
```
                               *                               
                              * *                              
                             *   *                             
                            * * * *                            
                           *       *                           
                          * *     * *                          
                         *   *   *   *                         
                        * * * * * * * *                        
                       *               *                       
                      * *             * *                      
                     *   *           *   *                     
                    * * * *         * * * *                    
                   *       *       *       *                   
                  * *     * *     * *     * *                  
                 *   *   *   *   *   *   *   *                 
                * * * * * * * * * * * * * * * *                
               *                               *               
              * *                             * *              
             *   *                           *   *             
            * * * *                         * * * *            
           *       *                       *       *           
          * *     * *                     * *     * *          
         *   *   *   *                   *   *   *   *         
        * * * * * * * *                 * * * * * * * *        
       *               *               *               *       
      * *             * *             * *             * *      
     *   *           *   *           *   *           *   *     
    * * * *         * * * *         * * * *         * * * *    
   *       *       *       *       *       *       *       *   
  * *     * *     * *     * *     * *     * *     * *     * *  
 *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   * 
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
```

3. Find the number of entries which are not divisible by 
a prime number in the first n rows of Pascal'striangle:

```bash
make not-div-count NUM=100 DIVIDER=7
```
```
2361
```

```bash
make not-div-count NUM=1000000000 DIVIDER=7
```
```
2129970655314432
```

### Tests

* To run all tests without coverage
```bash
$ python -m unittest discover -s tests
```

* To tun tests with coverage
```bash
coverage run -m unittest discover -s tests
```

* To check coverage report
```bash
coverage report
```

* To create detailed presentation and view it with a browser
```bash
coverage html && python -m webbrowser "htmlcov/index.html"
```
[Theory]: docs/pascal_triangle_divisibility_problem.pdf
[Docker Install]:  https://docs.docker.com/install/