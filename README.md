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

### Usage

1. To display Pascal's triangle:
```bash
$ make pascal-triangle NUM=5
```
where `NUM` is the number of rows

An alternative docker command:

```bash
$ docker run --rm -it pascal-triangle pascal-triangle -n 5
```

2. To display Sierpinski's triangle:
```bash
$ make sierpinski-triangle NUM=100 DIVIDER=7
```
where `NUM` is the number of rows

An alternative docker command:

```bash
$ docker run --rm -it pascal-triangle sierpinski-triangle -n 100 -d 7
```

3. To find the number of entries which are not divisible by 
a prime number in the first n rows of Pascal'striangle:
```bash
$ make not-div-count NUM=1000000000 DIVIDER=7
```
where `NUM` is the number of rows, `DIVIDER` is the prime number.

An alternative docker command:

```bash
$ docker run --rm -it pascal-triangle not-div-count -n 1000000000 -d 7
```

### Examples

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

```bash
$ make sierpinski-triangle NUM=54 DIVIDER=3
```
```
                                                     *                                                     
                                                    * *                                                    
                                                   * * *                                                   
                                                  *     *                                                  
                                                 * *   * *                                                 
                                                * * * * * *                                                
                                               *     *     *                                               
                                              * *   * *   * *                                              
                                             * * * * * * * * *                                             
                                            *                 *                                            
                                           * *               * *                                           
                                          * * *             * * *                                          
                                         *     *           *     *                                         
                                        * *   * *         * *   * *                                        
                                       * * * * * *       * * * * * *                                       
                                      *     *     *     *     *     *                                      
                                     * *   * *   * *   * *   * *   * *                                     
                                    * * * * * * * * * * * * * * * * * *                                    
                                   *                 *                 *                                   
                                  * *               * *               * *                                  
                                 * * *             * * *             * * *                                 
                                *     *           *     *           *     *                                
                               * *   * *         * *   * *         * *   * *                               
                              * * * * * *       * * * * * *       * * * * * *                              
                             *     *     *     *     *     *     *     *     *                             
                            * *   * *   * *   * *   * *   * *   * *   * *   * *                            
                           * * * * * * * * * * * * * * * * * * * * * * * * * * *                           
                          *                                                     *                          
                         * *                                                   * *                         
                        * * *                                                 * * *                        
                       *     *                                               *     *                       
                      * *   * *                                             * *   * *                      
                     * * * * * *                                           * * * * * *                     
                    *     *     *                                         *     *     *                    
                   * *   * *   * *                                       * *   * *   * *                   
                  * * * * * * * * *                                     * * * * * * * * *                  
                 *                 *                                   *                 *                 
                * *               * *                                 * *               * *                
               * * *             * * *                               * * *             * * *               
              *     *           *     *                             *     *           *     *              
             * *   * *         * *   * *                           * *   * *         * *   * *             
            * * * * * *       * * * * * *                         * * * * * *       * * * * * *            
           *     *     *     *     *     *                       *     *     *     *     *     *           
          * *   * *   * *   * *   * *   * *                     * *   * *   * *   * *   * *   * *          
         * * * * * * * * * * * * * * * * * *                   * * * * * * * * * * * * * * * * * *         
        *                 *                 *                 *                 *                 *        
       * *               * *               * *               * *               * *               * *       
      * * *             * * *             * * *             * * *             * * *             * * *      
     *     *           *     *           *     *           *     *           *     *           *     *     
    * *   * *         * *   * *         * *   * *         * *   * *         * *   * *         * *   * *    
   * * * * * *       * * * * * *       * * * * * *       * * * * * *       * * * * * *       * * * * * *   
  *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *  
 * *   * *   * *   * *   * *   * *   * *   * *   * *   * *   * *   * *   * *   * *   * *   * *   * *   * * 
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

```

[Theory]: docs/pascal_triangle_divisibility_problem.pdf
[Docker Install]:  https://docs.docker.com/install/