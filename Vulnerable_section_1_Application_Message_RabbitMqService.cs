 ﻿using System.Text;
 using Newtonsoft.Json;
 using RabbitMQ.Client;
 
         public RabbitMqService(string queueName)
         {
             _queueName = queueName;
             var factory = new ConnectionFactory()
             {
                HostName = "localhost",
                UserName = "admin",
                Password = "Abc@1234",
                VirtualHost = "/"
             };
             var conn = factory.CreateConnection();
             _channel = conn.CreateModel();
             _channel.QueueDeclare(_queueName, true);

         }
 
         public void SendMessage<T>(T message)