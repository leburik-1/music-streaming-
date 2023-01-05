public class AudioServeTask implements Runnable
{
   private static final String audioURL;
   private File soundFile;
   
   public AudioServeTask(String url)
   {
      this.audioURL = url;
   }
   
   public void run()
   {
     try 
     {
        soundFile = File(audioURL);
        try (ServerSocket serverSocket = new ServerSocket(5874))
        {
           FileInputStream in = new FileInputStream(soundFile);
           if (serverSocker.isBound()) {
              Socket client = serverSocker.accept();
              OutputStream out = client.getOutputStream();
              
              byte buffer[] = new byte[2048];
              int count;
              while ((count = in.read(buffer)) != -1)
                  out.write(buffer,0,count);
           }
        }
        
        System.out.println("server: shutdown");
     } 
     catch (InterruptedException exception)
     {
        exception.printStackTrace();
        Thread.currentThread().interrupt();
     }
   }
}
