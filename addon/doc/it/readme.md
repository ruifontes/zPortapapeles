# Manuale di zAppunti

Questo componente aggiuntivo prende spunto dal componente aggiuntivo Fake Clipboard.

Con zAppunti si possono ascoltare gli annunci delle combinazioni di tasti per copia, incolla, annulla, taglia e seleziona tutto.

Nel componente è stata inclusa la possibilità di attivare o disattivare dei suoni che rafforzano i messaggi così come una cronologia con la quale possiamo copiare un appunto nel focus corrente.

## Gesti di immissione...

Nella sezione Gesti e Tasti di Immissione di NVDA, se cerchiamo la categoria zAppunti, possiamo aggiungere una combinazione di tasti che non è assegnata di default alla cronologia per visualizzarne la finestra di dialogo.

Si trova anche una sezione nella 	quale possiamo modificare i tasti di attivazione assegnati agli appunti, questa sezione si deve modificare solo se la nostra lingua o il nostro sistema hanno tasti differenti assegnati di default agli appunti.

## Opzioni del componente

Nelle impostazioni di NVDA nella categoria Opzioni di zAppunti, possiamo attivare o disattivare attraverso caselle di controllo sia se vogliamo suoni che se vogliamo che la cronologia sia attivata, possiamo anche scegliere se vogliamo ricevere o meno messaggi vocali.

Se la casella di controllo della cronologia è attivata, avremo una casella combinata in cui scegliere il tempo di monitoraggio degli appunti e una casella da attivare o disattivare se vogliamo un suono quando qualcosa viene aggiunto alla cronologia.

Se la casella di controllo è disattivata, sia la casella combinata che la possibilità di scegliere se vogliamo suoni nella cronologia non verranno visualizzate.

Si noti che se iniziamo a ricevere errori negli appunti, è conveniente aumentarne il tempo di monitoraggio.

## Finestra della cronologia

Dobbiamo assegnare in gesti e tasti di immissione una combinazione di tasti a questa finestra di dialogo  che non è assegnata per impostazione predefinita.

La finestra di dialogo si aprirà soltanto se conterrà almeno una voce salvata, finché non avrà voci non saremo in grado di aprirla.

Saremo informati sia attraverso messaggi informativi sia se la finestra è già aperta.

Una volta aperta, la finestra di dialogo contiene l'elenco delle voci ed i 4 pulsanti seguenti:

* Elimina o Alt+E: se si preme questo pulsante, verrà eliminata la voce sulla quale ci troviamo.

* Elimina tutto o Alt+T: verranno eliminate tutte le voci della cronologia.

* Aggiorna o Alt+A: aggiorna la cronologia con le nuove voci aggiunte, funziona bene se aggiungiamo voci alla cronologia mentre la finestra di dialogo è aperta.

* Chiudi o Alt+C, Esc o Alt+F4: chiude la finestra di dialogo della cronologia.

Quando ci troviamo nell'elenco, se premiamo INVIO, la voce evidenziata verrà copiata nell'applicazione che si trova dietro alla finestra di dialogo della cronologia.

Ad esempio, se abbiamo aperto il blocco note, apriamo la cronologia e premiamo INVIO sulla prima voce, l'elemento che abbiamo selezionato verrà copiato nel blocco note.

## Limitazioni di zAppunti

zAppunti non è compatibile con altri componenti installati che fanno la stessa cosa come Fake Clipboard o Clipspeak. Potrebbero essercene altri ed in questo caso dovremo disabilitarli se vogliamo utilizzare zAppunti.

Si tenga presente che le voci della cronologia verranno eliminate al riavvio di NVDA.

La cronologia degli appunti di Windows potrebbe avere voci duplicate se utilizziamo la cronologia di zClipboard. Si dovrà scegliere quale si vorrà utilizzare.

## Ringraziamenti

* Javi Domínguez: Per il suo aiuto disinteressato e per aver contribuito alla funzione di monitoraggio degli appunti.
* Portoghese Brasiliano: pedro-hdias
* Russo: Valentin Kupriyanov
* Italiano: Alessio Lenzi

# Registro delle modifiche.
## Versione 0.3.

* Aggiunto il rilevamento della selezione del testo durante la copia.

* Aggiunta la possibilità di disabilitare e abilitare rapidamente le funzioni del componente per quanto riguarda gli appunti.

* Aggiunto il supporto delle tastiere che utilizzano caratteri cirillici.

* Aggiunte le lingue portoghese brasiliano, russo, portoghese e italiano.

## Versione 0.2.

* Modificate tutte le funzioni degli appunti in cTypes

Adesso gli appunti verranno gestiti direttamente con le funzioni di sistema evitando di utilizzare le funzioni NVDA e wxpython.

* Il componente è pronto per essere tradotto.

## Versione 0.1.5.

* Pronuncia ciò che è stato copiato negli appunti e aggiunto alla cronologia.

Se abbiamo attivato l'opzione Attiva o disattiva la cronologia degli appunti nelle opzioni del componente, ora avremo questa nuova opzione.

Con questa opzione, ciò che è stato copiato nella cronologia o se è già nella cronologia, l'ultima copia negli appunti verrà letta con NVDA.

Verrà menzionata solo l'ultima stringa copiata e solo una volta per non saturare fino a quando non verrà ripetuta un'altra stringa copiata, la precedente non verrà ripetuta.

* Gli appunti verranno cancellati quando si avvia il componente per la prima volta.

Adesso non verrà più copiato ciò che avevamo negli appunti quando si avvia NVDA, gli appunti verranno avviati puliti.

Ciò non influisce con la cronologia degli appunti di Windows.

*** Attenzione: dobbiamo tenere conto di questo, poiché se abbiamo qualcosa di importante negli appunti potrebbe essere cancellata. ***

## Versione 0.1.4.

* Modificato il modo per ottenere i dati degli appunti.

## Versione 0.1.3.

* La versione minima di NVDA per utilizzare il componente è la 2021.2.

* Aggiunte le opzioni per la cronologia.

Adesso è possibile scegliere il tempo di monitoraggio e se vogliamo un suono quando qualcosa viene copiato nella cronologia.

* Aggiunto il supporto in Word ed Excel per non annunciare le combinazioni degli appunti.

* Gli appunti sono ora monitorati, quindi qualsiasi componente che copia negli appunti è ora supportato, anche la copia da NVDA per inserire nel focus

## Versione 0.1.2.

* Aggiunto Abilita o disabilita gli annunci vocali nelle opzioni del componente

Nelle applicazioni consentite, ometterà i messaggi corrispondenti ai tasti degli appunti.

## Versione 0.1.1.

* Modificato il modo di gestire le acquisizioni negli appunti e la loro gestione.

* Risolto il bug che lasciava gli appunti aperti.

## Versione 0.1.

* Versione iniziale.