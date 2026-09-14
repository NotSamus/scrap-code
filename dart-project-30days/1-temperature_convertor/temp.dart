// This is for user input 
import 'dart:io';

void main(){
    stdout.write('Enter temperature: ');
    String? input = stdin.readLineSync();
    var temperature = double.tryParse(input?.trim()?? '');
    if (temperature == null){
        throw ArgumentError('Value must be a number!!!!');
    }
    print('the temperature is $input');


    stdout.write('convert to F or C?');
    String? choice = stdin.readLineSync()?.trim().toLowerCase()?? '';
    double result;
    String unit;
    switch (choice){
        case 'f':
            result = temperature *9/5 +32;
            unit = 'F';
            break;
        case 'c':
            result = (temperature-32) *5/9;
            unit = 'C';
            break;
        default:
            print('enter a valid option...');
            return;

    }
    
    print('final $temperature ${unit =='F'?'C':'F'} is $result $unit');

}