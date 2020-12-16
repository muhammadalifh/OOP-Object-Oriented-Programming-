# Soal
1.) Buktikan bahwa abstract method memastikan bahwa method tersebut di-override oleh subclass. 

2.) Buktikan bahwa objek dari abstract class tidak dapat dibentuk.

# Jawab
1.) Jika dilihat pada Source Code-nya, Pada **Class(Permainan)** terdapat Fungsi **_PermainanMethod_** dimana fungsi tersebut adalah fungsi dari **Abstract Method**

`from abc import ABC,abstractmethod`

![1 2](https://user-images.githubusercontent.com/61005674/102381028-4c0a0b80-3ffb-11eb-92d9-40db1073db58.png)

Setelah itu kita bisa lihat Fungsi Tersebut berada di dalam Sub-class yaitu **Class Arcade** dan **Class Strategy**

![2 1](https://user-images.githubusercontent.com/61005674/102381484-e0746e00-3ffb-11eb-92a6-7ed45cb291e1.png)

![3 1](https://user-images.githubusercontent.com/61005674/102381678-19acde00-3ffc-11eb-8e71-145f1a69458a.png)

Terlihat pada 2 Gambar Diatas, pada masing-masing Sub-class Sudah ada **_PermainanMethod_** yang berasal dari **Abstract Method**. Ini berarti dari **Abstract Method** yang sudah di buat pada **Abstract Class** terbukti bahwa telah ditimpa / _Overriding_. Karena jika **Abstract Method** tidak di  _Override_ maka akan terjadi Error.

2.) **Abstract Class** adalah class yang masih dalam bentuk abstrak. Karena bentuknya masih abstrak, dia tidak bisa dibuat langsung menjadi objek. Sebuah class agar dapat disebut class abstrak setidaknya memiliki satu atau lebih method abstrak. Karena disini saya menggunakan bahasa python, jadi **Abstract Class** tidak bisa langsung di gunakan. tetapi harus meng-import terlebih dahulu Abstract Base Class (ABC), jika sudah di-import barulah **Abstract Class** bisa di gunakan. dan jika dilihat pada Gamabar pertama juga terlihat bahwa terdapat **decorator** yang bernama **@abstractmethod**, hal ini di gunakan untuk membuat **Abstract Method** pada fungsi tersebut.
