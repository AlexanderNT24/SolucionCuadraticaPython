#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <fstream>
#include <string>


using namespace std;

struct valores {
	char dato;
	valores* siguiente;
	valores* atras;
}*primeroValor, * ultimoValor;

struct ecuaciones {
	string ecuacion;
	string x1;
	string x2;
	ecuaciones* siguienteEcuaciones;
	ecuaciones* atrasEcuaciones;
}*primeroEcuaciones, * ultimoEcuaciones;

string terminoCuadraticoString;
string terminoLinealString;
string terminoIndependienteString;

string parteA;
string parteB;
string parteC;

float x1;
float x2;

float terminoCuadratico;
float terminoLineal;
float terminoIndependiente;

void principal();

void actualizarLista();
bool buscarArchivos(string);

void resolverEcuacion(string);
void ingresarCuadratica(string);
void castearCuadratica();
void casteoCuadraticaTerminos();
void resolverCuadratica();
void escribirArchivo();
void escribirArchivoError();
void actualizarArchivo(string);

int main() {
	principal();
}

void principal() {
	
	ifstream archivo;
	string cuadratica;
	
	//"D:/Pyhton/archivos"
	
	archivo.open("D:\\SolucionCuadraticaPython\\archivos\\archivo.txt", ios::in);
	
	if (archivo.fail()) {
		cout << "Error";
		
	}
	else {
		getline(archivo, cuadratica);
		cout << cuadratica << endl;
	}
	archivo.close();
	actualizarLista();
	if (buscarArchivos(cuadratica))
	{
		cout << "\nCondicional";
		
		escribirArchivo();
	}
	else {
		resolverEcuacion(cuadratica);
	}
}

void actualizarLista() {
	cout << "Recuperar Archivos" << endl;
	string cadena;
	ifstream archivo;
	archivo.open("D:\\SolucionCuadraticaPython\\archivos\\respuestas.txt", ios::in);
	if (archivo.fail()) {
		cout << "Error al recuperar";
		
	}
	else
					 while (!archivo.eof()) {
						 ecuaciones* nuevo = new ecuaciones();
						 if (primeroEcuaciones == NULL) {
							 primeroEcuaciones = nuevo;
							 primeroEcuaciones->siguienteEcuaciones = NULL;
							 primeroEcuaciones->atrasEcuaciones = NULL;
							 ultimoEcuaciones = primeroEcuaciones;
						 }
						 else {
							 ultimoEcuaciones->siguienteEcuaciones = nuevo;
							 nuevo->siguienteEcuaciones = NULL;
							 nuevo->atrasEcuaciones = ultimoEcuaciones;
							 ultimoEcuaciones = nuevo;
						 }
						 
						 archivo >> nuevo->ecuacion;
						 //nvuevo
						 archivo >> nuevo->x1;
						 archivo >> nuevo->x2;
						 cadena = nuevo->ecuacion +"\nx1:"+ nuevo->x1 +"\nx2:"+ nuevo->x2;
						 
						 cout <<"Cadena "<< cadena << endl;
	}
					 archivo.close();
					 
}

bool buscarArchivos(string ecuacion) {
	ecuaciones* actual = new ecuaciones();
	actual = primeroEcuaciones;
	int i = 0;
	if (primeroEcuaciones != NULL) {
		while (actual != NULL)
		{
			i++;
			if (actual->ecuacion == ecuacion) {
				x1=atof(actual->x1.c_str());
				x2=atof(actual->x2.c_str());
				return true;
			}
			actual = actual->siguienteEcuaciones;
		}
	}
	else {
		cout << "\nLista vacia";	
	}
	return false;
}

void resolverEcuacion(string cuadratica) {
	try {
		ingresarCuadratica(cuadratica);
		castearCuadratica();
		casteoCuadraticaTerminos();
		resolverCuadratica();
		escribirArchivo();
		actualizarArchivo(cuadratica);
	}
	catch (exception& e) {
		escribirArchivoError();
	}
}

void ingresarCuadratica(string cuadratica) {
	int contador = 0;
	while (cuadratica[contador] != NULL)
	{
		valores* nuevo = new valores();
		if (primeroValor == NULL) {
			primeroValor = nuevo;
			primeroValor->siguiente = NULL;
			primeroValor->atras = NULL;
			ultimoValor = primeroValor;
		}
		else {
			ultimoValor->siguiente = nuevo;
			nuevo->siguiente = NULL;
			nuevo->atras = ultimoValor;
			ultimoValor = nuevo;
		}
		nuevo->dato = cuadratica[contador];
		contador++;
	}
}

void castearCuadratica() {
	valores* actual = new valores;
	actual = primeroValor;
	if (primeroValor != NULL) {
		cout << "\nEntro A";
		parteA = parteA + actual->dato;
		actual = actual->siguiente;
		while (actual != NULL)
		{
			if (actual->dato == '-' || actual->dato == '+')
			{
				parteB = parteB + actual->dato;
				actual = actual->siguiente;
				break;
			}
			else {
				cout << "\n" << actual->dato;
				parteA = parteA + actual->dato;
			}
			actual = actual->siguiente;
			
		}
		cout << "\nEntro B";
		while (actual != NULL)
		{
			if (actual->dato == '-' || actual->dato == '+')
			{
				parteC = parteC + actual->dato;
				actual = actual->siguiente;
				break;
			}
			else {
				cout << "\n" << actual->dato;
				parteB = parteB + actual->dato;
			}
			actual = actual->siguiente;
		}
		cout << "\nEntro C";
		while (actual != NULL)
		{
			if (actual->dato == '=')
			{
				break;
				
			}
			else {
				cout << "\n" << actual->dato;
				parteC = parteC + actual->dato;
			}
			actual = actual->siguiente;
		}
	}
	cout << "\nParte A:" << parteA;
	cout << "\nParte B:" << parteB;
	cout << "\nParte C:" << parteC;
	
}
void casteoCuadraticaTerminos() {
	int contador = 0;
	while (parteA[contador] != NULL)
	{
		if (parteA[contador] == 'x')
		{
			break;
		}
		else {
			terminoCuadraticoString = terminoCuadraticoString + parteA[contador];
			contador++;
		}
		
	}
	terminoCuadratico = atof(terminoCuadraticoString.c_str());
	contador = 0;
	while (parteB[contador] != NULL)
	{
		
		if (parteB[contador] == 'x')
		{
			break;
		}
		else {
			terminoLinealString = terminoLinealString + parteB[contador];
			contador++;
		}
	}
	terminoLineal = atof(terminoLinealString.c_str());
	contador = 0;
	while (parteC[contador] != NULL)
	{
		if (parteC[contador] == '=')
		{
			break;
		}
		else {
			terminoIndependienteString = terminoIndependienteString + parteC[contador];
			contador++;
		}
	}
	terminoIndependiente = atof(terminoIndependienteString.c_str());
	if (terminoCuadratico==0)
	{
		terminoCuadratico=1;
	}
	cout << "\nA:" << terminoCuadratico;
	cout << "\nB:" << terminoLineal;
	cout << "\nC:" << terminoIndependiente << endl;
}
void resolverCuadratica() {
	float x = (terminoLineal * terminoLineal) - (4 * terminoCuadratico * terminoIndependiente);
	
	if (x <= 0) {
		x = x * (-1);
		cout << "Solución solo en números complejos" << endl;
		ofstream fichero("D:/SolucionCuadraticaPython/archivos/respuesta.txt");
		fichero << "Solución en los complejos" << endl;
		fichero.close();
		exit(0);
	}
	else {
		
		x1 = (-terminoLineal + sqrt(x)) / (2 * terminoCuadratico);
		x2 = (-terminoLineal - sqrt(x)) / (2 * terminoCuadratico);
		
		cout << "x1 = " << x1 << endl;
		cout << "x2 = " << x2 << endl;
	}
}
void escribirArchivo() {
	ofstream fichero("D:/SolucionCuadraticaPython/archivos/respuesta.txt");
	fichero << "X1=" << x1 << endl;
	fichero << "X2=" << x2 << endl;
	fichero.close();
}

void escribirArchivoError() {
	ofstream fichero("D:/SolucionCuadraticaPython/archivos/respuesta.txt");
	fichero << "Lo sentimos no podemos solucionar" << endl;
	fichero << "" << endl;
	fichero.close();
	
}


void actualizarArchivo(string cuadratica) {
	fstream ficheroRespuestas;
	ficheroRespuestas.open("D:/SolucionCuadraticaPython/archivos/respuestas.txt", fstream::app);
	ficheroRespuestas <<"\n"<< cuadratica << endl;
	ficheroRespuestas << x1 << endl;
	ficheroRespuestas << x2;
	ficheroRespuestas.close();
}
