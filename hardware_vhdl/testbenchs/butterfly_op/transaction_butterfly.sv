
class Transaction;

    int width = 8
    rand bit[width-1:0] left, rght, modulo;
    
    constraint ct_modulo    {modulo > 0 ; modulo < 2**width}
    constraint ct_left      {left > 0 ; left < 2**width}
    constraint ct_left      {rght > 0 ; rght < 2**width}

    virtual function void display();
        $write("left=%d, rght=%d, modulo=%d", left, rght, modulo);
    endfunction
    
    virtual function Transaction copy();
        Transaction copy;
        copy.left   = this.left;
        copy.rght   = this.rght;
        copy.modulo = this.modulo;
        return copy;
    endfunction
endclass
