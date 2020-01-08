import unittest

from src.lib.triangles import PascalTriangle, SierpinskiTriangle


class TestPascalTriangle(unittest.TestCase):
    n = 12
    repr = """
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
  1 10 45 120 210 252 210 120 45 10 1  
1 11 55 165 330 462 462 330 165 55 11 1
"""

    tests = [
        {
            'n': 5,
            'triangle': [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
            ],
        },
        {
            'n': 11,
            'triangle': [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
                [1, 5, 10, 10, 5, 1],
                [1, 6, 15, 20, 15, 6, 1],
                [1, 7, 21, 35, 35, 21, 7, 1],
                [1, 8, 28, 56, 70, 56, 28, 8, 1],
                [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
                [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1],
            ],
        },
    ]

    def test_triangle(self):
        for test in self.tests:
            self.assertListEqual(test['triangle'], PascalTriangle(test['n']).triangle)

    def test_repr(self):
        # We should remove the first and last '\n' from self.repr
        self.assertEqual(self.repr[1:-1], repr(PascalTriangle(self.n)))


class TestSierpinskiTriangle(unittest.TestCase):
    n_1 = 16
    d_1 = 2
    repr_1 = """
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
"""

    n_2 = 27
    d_2 = 3
    repr_2 = """
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
"""

    n_3 = 30
    d_3 = 7
    repr_3 = """
                             *                             
                            * *                            
                           * * *                           
                          * * * *                          
                         * * * * *                         
                        * * * * * *                        
                       * * * * * * *                       
                      *             *                      
                     * *           * *                     
                    * * *         * * *                    
                   * * * *       * * * *                   
                  * * * * *     * * * * *                  
                 * * * * * *   * * * * * *                 
                * * * * * * * * * * * * * *                
               *             *             *               
              * *           * *           * *              
             * * *         * * *         * * *             
            * * * *       * * * *       * * * *            
           * * * * *     * * * * *     * * * * *           
          * * * * * *   * * * * * *   * * * * * *          
         * * * * * * * * * * * * * * * * * * * * *         
        *             *             *             *        
       * *           * *           * *           * *       
      * * *         * * *         * * *         * * *      
     * * * *       * * * *       * * * *       * * * *     
    * * * * *     * * * * *     * * * * *     * * * * *    
   * * * * * *   * * * * * *   * * * * * *   * * * * * *   
  * * * * * * * * * * * * * * * * * * * * * * * * * * * *  
 *             *             *             *             * 
* *           * *           * *           * *           * *
"""

    tests = [
        {
            'n': 10,
            'd': 2,
            'triangle': [
                [1],
                [1, 1],
                [1, 0, 1],
                [1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 0, 0, 1, 1],
                [1, 0, 1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],

            ],
        },
        {
            'n': 15,
            'd': 3,
            'triangle': [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 0, 0, 1],
                [1, 1, 0, 1, 1],
                [1, 2, 1, 1, 2, 1],
                [1, 0, 0, 2, 0, 0, 1],
                [1, 1, 0, 2, 2, 0, 1, 1],
                [1, 2, 1, 2, 1, 2, 1, 2, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                [1, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1],
                [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                [1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                [1, 2, 1, 1, 2, 1, 0, 0, 0, 1, 2, 1, 1, 2, 1],

            ],
        },
        {
            'n': 30,
            'd': 7,
            'triangle': [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
                [1, 5, 3, 3, 5, 1],
                [1, 6, 1, 6, 1, 6, 1],
                [1, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 1, 1],
                [1, 2, 1, 0, 0, 0, 0, 1, 2, 1],
                [1, 3, 3, 1, 0, 0, 0, 1, 3, 3, 1],
                [1, 4, 6, 4, 1, 0, 0, 1, 4, 6, 4, 1],
                [1, 5, 3, 3, 5, 1, 0, 1, 5, 3, 3, 5, 1],
                [1, 6, 1, 6, 1, 6, 1, 1, 6, 1, 6, 1, 6, 1],
                [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 1],
                [1, 2, 1, 0, 0, 0, 0, 2, 4, 2, 0, 0, 0, 0, 1, 2, 1],
                [1, 3, 3, 1, 0, 0, 0, 2, 6, 6, 2, 0, 0, 0, 1, 3, 3, 1],
                [1, 4, 6, 4, 1, 0, 0, 2, 1, 5, 1, 2, 0, 0, 1, 4, 6, 4, 1],
                [1, 5, 3, 3, 5, 1, 0, 2, 3, 6, 6, 3, 2, 0, 1, 5, 3, 3, 5, 1],
                [1, 6, 1, 6, 1, 6, 1, 2, 5, 2, 5, 2, 5, 2, 1, 6, 1, 6, 1, 6, 1],
                [1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 1, 1],
                [1, 2, 1, 0, 0, 0, 0, 3, 6, 3, 0, 0, 0, 0, 3, 6, 3, 0, 0, 0, 0, 1, 2, 1],
                [1, 3, 3, 1, 0, 0, 0, 3, 2, 2, 3, 0, 0, 0, 3, 2, 2, 3, 0, 0, 0, 1, 3, 3, 1],
                [1, 4, 6, 4, 1, 0, 0, 3, 5, 4, 5, 3, 0, 0, 3, 5, 4, 5, 3, 0, 0, 1, 4, 6, 4, 1],
                [1, 5, 3, 3, 5, 1, 0, 3, 1, 2, 2, 1, 3, 0, 3, 1, 2, 2, 1, 3, 0, 1, 5, 3, 3, 5, 1],
                [1, 6, 1, 6, 1, 6, 1, 3, 4, 3, 4, 3, 4, 3, 3, 4, 3, 4, 3, 4, 3, 1, 6, 1, 6, 1, 6, 1],
                [1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 1, 1],
            ],
        },
    ]

    def test_triangle(self):
        for test in self.tests:
            self.assertListEqual(test['triangle'], SierpinskiTriangle(test['n'], test['d']).triangle)

    def test_repr(self):
        # We should remove the first and last '\n' from self.repr
        self.assertEqual(self.repr_1[1:-1], repr(SierpinskiTriangle(self.n_1, self.d_1)))
        self.assertEqual(self.repr_2[1:-1], repr(SierpinskiTriangle(self.n_2, self.d_2)))
        self.assertEqual(self.repr_3[1:-1], repr(SierpinskiTriangle(self.n_3, self.d_3)))


if __name__ == '__main__':
    unittest.main()
