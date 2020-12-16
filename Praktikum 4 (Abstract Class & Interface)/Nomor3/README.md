# Abtract Class #
Abstract Class merupakan Class yang khusus dibuat untuk keperluan inheritance.
Tujuan dari pembuatan abstract class ini ialah untuk membuat definisi umum bagi class-class yang akan menjadi turunan darinya.
Abstract Class tidak bisa diinstansiasi. Abstract method tidak mempunyai implementasi,
sehingga penulisannya dilakukan hanya dengan mengikutkan semikolon, bukan blok method {} seperti biasanya.
Abstract method ini bisa digunakan oleh Class turunannya dengan melakukan override.
 
# Interface #
Sedangkan interface secara filosofis lebih berfungsi sebagai antarmka yang membentuk komunikasi dengan code lain. 
Misalnya membentuk hubungan antara sebuah object dengan object yang lain atau hubungan antara object sebagai penyedia dengan code pengguna. 
Karena itulah interface ini banyak digunakan dalam dunia design pattern. Sebab kebanyakan dari design pattern ini menekankan hubungan antar object.

## PERBEDAAN ANTARA CLASS ABSTRACT DAN INTERFACE ##


| No. |  Class Abstract  |  Interface  |
| --- | --- | --
|  1. |  Class Abstract dapat mempunyai abstract dan non abstract method   |  Interface hanya dapat mempunyai abstract  method|
|  2. |  Class Abstract tidak mendukung multiple Inheritance    |  Interface mendukung multiple Inheritance |
|  3. | Class Abstract mempunyai final ,non final dan static ,non static variable    |  Interface hanya mempunyai final dan static variable |
|  4. | Class Abstract dapat mengimplementasi Interface |  Interface tidak dapat mengimplementasi Class Abstract |
|  5. | Class Abstract dapat mempunyai ,static method ,main method dan Constructor |  Interface tidak dapat mempunyai ,static method ,main method dan Constructor |


Tetapi karena disini saya menggunakan bahasa python, maka sebenarnya Interface sendiri juga tidak terlalu di butuhkan.
ini karena Python memiliki multiple inheritance yang tepat, dan juga ducktyping.
Meskipun demikian, masih ada beberapa kegunaan Interface. Beberapa dari interface tersebut dicakup oleh Abstract Base Classes (ABC) Pythons, diperkenalkan pada Python 2.6. 
Hal ini, berguna kika ingin membuat base classes yang tidak dapat dibuat instance-nya, tetapi menyediakan interface atau bagian tertentu dari implementasinya.
