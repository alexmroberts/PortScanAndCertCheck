# Introduction
A script to check which ports are open for a website and check the SSL certificate for any secure ports. Using multiple threads to check so as to speed up the process.
  
  
You can make modifications to these variables to change the outcome of the scan:  

**max_threads** <- (int) By default is set to 10. You can change this to however many threads you want used. Decreasing this will result in longer runtimes  
**starting_port** <- (int) By default is set to 1. You can change this to whichever port you want to start the scan at.  
**max_port** <- (int) By default is set to 445. This can be changed to a different number and will act as the top limit. Must be higher than starting_port.  
**secure_ports** <- (int list) By default includes 22, 443, 465, 993, 995. This can be modified to include more or less ports. This list controls what ports will have the certificate checked.  
**print_errors** <- (bool) By default is set to False. This can be changed to True if you want to display the failed port connectionsor any other errors.  
**connection_timeout** <- (float) By default is set to 5.0. This can be increased or decreased depending on how long the connection should wait until it times out. Increasing this will result in longer runtimes but decreasing it too low could result in false positives.

