theysay
=======

中文：这是一个分布式的微博爬虫，正在开发中
=======

      1. black3:　    worker所在目录， 采用python 开发。
      2. mendor:      scheduler所在目录， 采用node.js。
      3. 磁盘数据库： 开发版使用mongodb, 采用mongoose作为API。 部署之后看情况决定是否采用hadoop。
      4. 内存数据库： 不采用redis,自己封装了一个。 原因： 进程间通信对于worker设计的方式来说， 有点浪费。
      5. Bloomfiler:  开发版暂时采用了一个开源的库，可能会换。
      6. Moniter:　　 采用Jquery， canjs(?), 以及一个grid开源库。 
      7. 进度：       目前只有一个人开发利用业余时间开发， 应该不会太快
      
      
