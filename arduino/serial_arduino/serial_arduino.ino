String inputString = "";

void serialEvent()
{
  char temp;
  
  while(Serial.available())
  {
    temp = (char)Serial.read();

    inputString += temp;    
    if(temp == '\n')
    {
      Serial.print(inputString);
      inputString = "";
    }   
  }
}

void setup()
{
  Serial.begin(9600);
}

void loop()
{
}
