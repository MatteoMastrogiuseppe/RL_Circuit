// inizializzazione
// float initial_condition;

void setup() {
  Serial.begin(9600);
  // initial_condition = analogRead(A0)*5/1024.;
  unsigned raw_initial_condition = analogRead(A0);
  unsigned raw_initial_condition;
  unsigned long t0;

}

void loop() {
  // put your main code here, to run repeatedly:
  // float tolerance = 0.1; //in volt
  int npt = 100; //numero di punti di acquisizione
  unsigned raw_tolerance = (unsigned) (0.01*1024/5.0); 
  unsigned long  array_time[npt]={};
  unsigned array_voltage[npt]={};
  
  //stop here until variation is < tolerance
  //while (fabs(analogRead(A0)*5/1024. - initial_condition) < tolerance)
  while (abs(analogRead(A0) - raw_initial_condition) < raw_tolerance)
    { t0 = micros();
    }

  // begin acquisition
  for (int i = 0; i < npt; i++){
    unsigned long now = micros();
    array_time[i] = (now - t0);
    unsigned raw_voltage = analogRead(A0);
    array_voltage[i] = raw_voltage;
  }

  for (int i = 0; i < npt; i++){
    Serial.print(array_time[i]);
    Serial.print(" ; ");
    Serial.println(array_voltage[i]/1024.*5);
  }

  //stop execution here
  while (1){
    
    }
}
