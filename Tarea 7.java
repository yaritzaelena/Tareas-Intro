
/////////Clase para la lista enlazad////////
public class ListaEnlazada {

    private Node primer;
    private Node ultimo;

    public ListaEnlazada(Node primer, Node ultimo) {
        this.primero = primer;
        this.ultimo = ultimo;
    }

    public ListaEnlazada() {
    }

    public Node getP() {
        return primer;
    }

    public void setP(Node primer) {
        this.primer = primer;
    }

    public Node getU() {
        return ultimo;
    }

    public void setU(Node ultimo) {
        this.ultimo = ultimo;
    }

    public void addInicio(int dato) {
        if (primer == null) {
            primer = new Node(dato, null);
            ultimo = primer;
        } else {
            Node nuevo = new Node(dato, primer);
            primer = nuevo;
        }
    }

    public void addFinal(int v) {
        if (ultimo == null) {
            ultimo = new Node(v, null);
            primero = ultimo;
        } else {
            ultimo.setSig(new Node(v, null));
            ultimo = ultimo.getSig();
        }
    }

    public int eliminarInicio() throws MyException {
        Node temp = primero;
        if (primer == null) {
            throw new MyException("La lista está vacía.");
        } else {
            primer = primer.getSig();
        }
        return temp.getData();
    }

    public int eliminarUltimo() throws MyException {
        Node temp = primero;
        int num = 0;
        if (temp == null) {
            throw new MyException("La lista está vacía.");
        }
        if (primero == ultimo) {
            num = ultimo.getData();
            primero = null;
            ultimo = null;
            return num;
        }
        while (temp != null) {
            if (temp.getSig() == ultimo) {
                num = temp.getSig().getData();
                ultimo = temp;
                ultimo.setSig(null);
            }
            temp = temp.getSig();
        }
        return num;
    }

    public void eliminarLista() throws MyException {
        if (primero == null) {
            throw new MyException("La lista ya está vacía.F");
        }
        primero = null;
        ultimo = null;
    }

    public String imprimir() throws MyException {
        if (primero == null) {
            throw new MyException("La lista está vacía.");
        }
        String txt = "";
        for (Node temp = primero; temp != null; temp = temp.getSig()) {
            txt += temp.getData() + " ";
        }

        return txt;
    }

    public int eliminarElemento(int dato) throws MyException {
        boolean flag = false;
        if (primero == null) {
            throw new MyException("La lista se encuentra vacía.");
        }
        if (primero.getData() == dato) {
            return eliminarInicio();
        }
        if (ultimo.getDato() == dato) {
            return eliminarUltimo();
        }
        for (Node temp = primero; temp.getSig() != null; temp = temp.getSig()) {
            if (temp.getSig().getData() == dato) {
                temp.setSig(temp.getSig().getSig());
                flag = true;
            }
        }
        if (flag == true) {
            return dato;
        } else {
            throw new MyException("El elemento no se encuentra en la lista.");
        }
    }

    public int eliminarIndice(int indice) throws MyException {
        if (primero == null) {
            throw new MyException("La lista se encuentra vacía.");
        }
        if (indice == 0) {
            return eliminarInicio();
        }
        Node temp = primero;
        for (int v = 1; v < indice; v++) {
            if (temp.getSig() == null) {
                throw new MyException("No se encontró un elemento con ese indice.");
            } else {
                temp = temp.getSig();
            }
        }
        int eliminado = temp.getSig().getData();
        temp.setSig(temp.getSig().getSig());
        if (temp.getSig() == null) {
            ultimo = temp;
        }
        return eliminado;
    }

    public int insertarOrd(int dato) {
        Node temp = primero;
        if (primero == null || dato < primero.getData()) {
            addInicio(dato);
            return dato;
        }
        if (dato > ultimo.getData()) {
            insertarFinal(dato);
            return dato;
        }
        while (temp != null) {
            if (dato < temp.getSig().getData()) {
                Node nuevo = new Node(dato, temp.getSig());
                temp.setSig(nuevo);
                return dato;
            }
            temp = temp.getSig();
        }
        return dato;
    }

    public void ordenarBurbuja() {
        boolean ordenado = true;
        Node actual;
        int datoTemp;
        do {
            actual = primero;
            ordenado = true;
            while (actual.getSig() != null) {
                if (actual.getData() > actual.getSig().getData()) {
                    datoTemp = actual.getData();
                    actual.setData(actual.getSig().getData());
                    actual.getSig().setDato(datoTemp);
                    ordenado = false;
                }
                actual = actual.getSig();
            }
        } while (ordenado != true);
    }
}
///////////Clase para el nodo///////
public class Node {
    private int dato;
    private Node sig;

    public Node(int dato, Node sig) {
        this.dato = dato;
        this.sig = sig;
    }

    public Node(int dato) {
        this.dato = dato;
    }

    public int getData() {
        return dato;
    }

    public void setData(int dato) {
        this.dato = dato;
    }

    public Node getSig() {
        return sig;
    }

    public void setSig(Node sig) {
        this.sig = sig;
    }

    @Override
    public String toString() {
        return "Node" + "dato=" + dato + ", sig=" + sig;
    }
    
    
}
