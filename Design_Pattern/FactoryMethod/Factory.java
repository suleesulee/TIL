package FactoryMethod;

public abstract class Factory {
    public final Product create(String owner){
        Product p = create(owner);
        registerProduct(p);
        return p;
    }
    protected abstract Product creaProduct(String owner);
    protected abstract void registerProduct(Product product);
    
}
