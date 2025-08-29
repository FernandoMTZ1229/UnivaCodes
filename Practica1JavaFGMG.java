package practicas;
import java.util.*;

public class Practica1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] numeros = new int[15];
		int num, contador_neg = 0, contador_positivos=0, result_promedio=0, suma_positivos=0;
		
		Scanner captura = new Scanner(System.in);
		
		for(int x = 0; x < numeros.length; x++) {
			System.out.println("Dame el valor: " + x);
			num = captura.nextInt();
			numeros[x] = num;
		}
		
		for(int i = 0; i < numeros.length; i ++) {
			//String n = numeros[i] %2 == 0 ? "hola" : "no";
			
			if(numeros[i] %2 == 0 && numeros[i] > 0) {
				double raiz;
				raiz = Math.sqrt(numeros[i]);
				System.out.println("La raiz cuadrada de " + numeros[i]+ " " +raiz);
			}
			
			if(numeros[i] < 0) {
				contador_neg += 1;
			
			}
			
			if(numeros[i] %2 !=0) {
				suma_positivos += numeros[i];
				contador_positivos += 1;
			}
			
		}
		result_promedio = suma_positivos / contador_positivos;
		
		System.out.println ("El resultado de negativo es:" +contador_neg);
		System.out.println("El promedio:" + result_promedio);

	}

}
