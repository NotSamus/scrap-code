void main(){
    print('Hello, Dart!');

    const name = 'Student';
    const language = 'dart';

    print('My name is, $name .');
    print('I am testing $language in VS code.');

    var numbers = [1,2,3];
    // This does not change the variables that are on the list
    for( final number in numbers){
        print(number);
    }

    // this does
    print('previous $numbers');
    for(var i = 0; i<numbers.length; i++){
        numbers[i] += 5;
    }  
    print('After $numbers');

    // print('---testing the maps on dart---');
    // Map<String, int> ages = {'Ana':20,'mike':10};
    // print('This print the ages: $ages');

}
