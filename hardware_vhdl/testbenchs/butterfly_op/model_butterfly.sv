
class Model;

    mailbox#(Transaction) gen2mdl, mdl2scr;
    
    function new(input mailbox#(Transaction) gen2mdl, input mailbox#(Transaction) mdl2scr);
        this.gen2mdl = gen2mdl;
        this.mdl2scr = mdl2scr;
    endfunction
    
    virtual task run();
        Transaction itr, otr;
        
        forever begin
            gen2mdl.get(itr);
            @ifc.cb;
            otr.rght   = (itr.left - itr.rght) % itr.modulo;
            otr.left   = (itr.left + itr.rght) % itr.modulo;
            otr.modulo = itr.modulo;
            mdl2scr.put(otr);
        end
    endtask

endclass
