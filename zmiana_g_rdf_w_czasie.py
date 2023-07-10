from subprocess import Popen

def main(XTC, TPR, index, XVG, begin, end, dt, atom):
    '''
    main(trajektoria analizowana, plik .tpr, indeks, output, poczatek, koniec obliczen, czas obliczenia RDF w ps, wokol ktorego atomu obliczany jest RDF)
    funkcja oblicza zmianę RDF w czasie, przy czym pomiar kolejnych RDFow nie naklada sie
    main('LUT_BCL60_md_1ps_plus15_50fs.xtc','LUT_BCL60_md_1ps_plus15_50fs.tpr','index_RDF_27022.ndx', 'otuput.xvg', '1500', '1550', '5', '10')
    '''
    import subprocess
    import pdb
    
    begin=int(begin)
    end=int(end)
    dt=int(dt)
    B = begin
    E = B + dt

    XVG=zmiana_rozszerzenia(XVG)

    while E<=end:
        print(E)
        XVG_zmienione = XVG+"_B"+str(B)+"_E"+str(E)+".xvg"
    #    print(XVG_zmienione) 
        
        p1 = subprocess.Popen(['echo', atom, '\n', 'SOL'], stdout=subprocess.PIPE)
#        pdb.set_trace()
        grdf= ' '.join(['g_rdf', '-f', XTC, '-s', TPR, '-n', index, '-b', str(B), '-e', str(E), '-o', XVG_zmienione])
        
        p2 = subprocess.Popen([grdf], stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
        p1.stdout.close()
        output = p2.communicate()[1]
    #    print(output)
        
        B = E
        E = E + dt

def zmiana_rozszerzenia(nazwa_pliku):
    '''
    - usuwa rozszerzenie .xvg
    - zwraca blad w razie innego rozszerzenia
    '''
    if nazwa_pliku[-4:] == ".xvg":
        nazwa_pliku = nazwa_pliku[0:-4]
        return(nazwa_pliku)
    elif nazwa_pliku[-4] =="." and nazwa_pliku[-3:] != "xvg":
        return("bledne rozszerzenie outputu, plik zostanie zapisany jako .xvg")
'''
def sub(aa):
    import subprocess
    import pdb
    p1 = subprocess.Popen(['echo','10\n','SOL'], stdout=subprocess.PIPE)
#    pdb.set_trace()
    p2 = subprocess.Popen(['g_rdf -f LUT_BCL60_md_1ps_plus15_50fs.xtc -s LUT_BCL60_md_1ps_plus15_50fs.tpr -n index_RDF_27022.ndx -b 1500 -e 1550 -o RDF_27022.xvg'],
                          stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
#['g_rdf -f', 'LUT_BCL60_md_1ps_plus15_50fs.xtc', '-s', 'LUT_BCL60_md_1ps_plus15_50fs.tpr', '-n', 'index_RDF_27022.ndx', '-b', '1500', '-e', '11000', '-o', 'RDF_27022.xvg'],
    p1.stdout.close()
    output = p2.communicate()[1]
    print(output)

def robota(bla):
    import subprocess
    import pdb
    p1 = subprocess.Popen(['echo', 'ala'], stdout=subprocess.PIPE)
#    pdb.set_trace()
    p2 = subprocess.Popen(['nano', 'ala.txt'], stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
    p1.stdout.close()
    output = p2.communicate()
    print(output)
def fun(a):
    from subprocess import Popen, PIPE
    output='dmesg | grep hda'
    # becomes
    p1 = Popen(["dmesg"], stdout=PIPE)
    p2 = Popen(["grep", "hda"], stdin=p1.stdout, stdout=PIPE)
    p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
    output = p2.communicate()
    return output
'''
