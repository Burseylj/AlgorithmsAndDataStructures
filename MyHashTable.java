import java.util.ArrayList;

public class MyHashTable<K,V> {
	private ArrayList<HashNode<K,V>> bucketArray;
	private int numBuckets;
	private int size;
	private double loadFactor;
	
	public MyHashTable() {
		this.size = 0;
		this.numBuckets = 10;
		this.loadFactor = 0.7;
		//fill empty bucket slots
		for (int i = 0; i<numBuckets; i++){
			this.bucketArray.add(null);
		}
	}
	
	public boolean isEmpty(){
		return size == 0;
	}

	public int getSize() {
		return size;
	}
	
	public V get(K key){
		//find head of linked list for key
		int index = bucketIndex(key);
		HashNode<K,V> head = bucketArray.get(index);
		//search linked list for key
		while (head != null) {
			if (head.getKey().equals(key)){
				return head.getValue();
			}
			head = head.getNext();
		}
		//if key not in table
		return null;
	}

	public V remove(K key) {
		//find head of linked list for key
		int index = bucketIndex(key);
		HashNode<K,V> head = bucketArray.get(index);
		HashNode<K,V> prev = null;
		//search linked list for key
		
		while (head != null) {
			if (head.getKey().equals(key)){
				break;
			}
			prev = head;
			head = head.getNext();
		}
		// if the key is not in the table
		if (head == null){
			return null;
		}
		//reduce size and remove key
		size--;
		if (prev == null){
			bucketArray.set(index, head);
		} else {
			prev.setNext(head.getNext());
		}
		return head.getValue();
	}
	
	public void add(K key, V value){
		//find head of linked list for key
		int index = bucketIndex(key);
		HashNode<K,V> newNode = new HashNode<K,V>(key,value);
		HashNode<K,V> head = bucketArray.get(index);
		//if bucketArray has no list at the hashed index
		if (head == null) {
			bucketArray.set(index,newNode);
			size++;
		}
		
		//search linked list for key
		while (head.getNext() != null) {
			if (head.getKey().equals(key)){
				head.setValue(value);
				return;
			}
			head = head.getNext();
		}
		//if key not in table, put node at end of list
		head.setNext(newNode);
		size++;
		
		//if bucketArray gets too big, resize it
		if (size*1.0/numBuckets > loadFactor) {
				doubleSize();
			}
		
		}
	private void doubleSize(){
		//double number of buckets, create new arraylist to hold them
		numBuckets *= 2;
		ArrayList<HashNode<K, V>> oldBucketArray = bucketArray;
		bucketArray = new ArrayList<HashNode<K, V>>();
		for (int i = 0; i<numBuckets;i++){
			bucketArray.add(null);
		}
		for (HashNode<K,V> node : oldBucketArray){
			HashNode<K,V> head = node;
			while (head != null){
				add(head.getKey(),head.getValue());
				head = head.getNext();
			}
		}
	}
	
	
	
	private int bucketIndex(K key){
		int hashCode = key.hashCode();
		int index = hashCode % numBuckets; //keep hash code inside the buckets
		return index;
	}
	
	


	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
}
