# zPano Kılavuzu:

Bu eklenti, Fake Clipboard eklentisinin tabanına sahiptir.  

zPano ile kopyalama, yapıştırma, geri alma, kesme ve tümünü seçme işlemleri için ilgili kısa yol tuşlarına bastığımızda bildirim duyarız.  

Mesajları güçlendiren sesleri etkinleştirme ve devre dışı bırakma imkanının yanı sıra odağı kopyalayabileceğimiz bir geçmiş penceresi de eklentiye dahil edildi.  

## Girdi hareketleri...

NVDA Girdi Hareketleri... bölümünde, zPano kategorisini ararsak, Geçmiş penceresini görüntülemek için  varsayılan olarak atanmamış bir tuş kombinasyonu ekleyebiliriz.  

Ayrıca panoya atıfta bulunulan tetik tuşlarını değiştirebileceğimiz bir bölümümüz olacak, bu bölüm ancak dilimiz veya sistemimiz panoya varsayılan olarak atanmış başka tuşlara sahipse değiştirilebilir.  

## Eklenti Seçenekleri:  

NVDA>Tercihler>Ayarlar iletişim kutusu içerisinde bulunan zPano seçeneklerinde, hem sesli bildirim istiyorsak hem de geçmişin etkinleştirilmesini istiyorsak onay kutularından etkinleştirip devre dışı bırakabiliriz, ayrıca Ses çalma özelliğini de isteyip istemediğimizi seçebiliriz.  

Geçmiş onay kutusu etkinleştirilirse, pano izleme süresini seçebileceğimiz bir seçim kutusu, geçmişe bir öğe eklendiğinde ses çalınmasını istersek de bir başka onay kutusu daha olacaktır.  

Geçmişi etkinleştir onay Kutusunun seçimi kaldırılırsa, hem birleşik seçim kutusu hem de geçmişte ses isteyip istemediğimizi seçme özelliği görünmez.  

Pano hatalarını almaya başlarsak pano izleme süresini artırmanın uygun olduğunu unutmamalıyız.  

## Geçmiş İletişim Kutusu:  

Pano geçmişi iletişim kutusu için varsayılanda kısa yol atanmamıştır. Görüntülüyebilmek için Girdi hareketleri içerisinden bir tuş  atamamız gerekir.  

Geçmiş içerisinde görebileceğimiz öğeler varsa bu iletişim kutusunu açabiliriz. Aksi taktirde açılmaz.  

İletişim kutusu açıldığında, geçmiş öğelerinin  bulunduğu liste ve aşağıdaki 4 düğmeden oluşur:  

* Sil Alt+S: Bu düğmeye basarsak, listede odaklanılan girişi siler.
* Tümünü Sil Alt+T: Tüm geçmiş girdilerini siler.
* Yenile Alt+Y: Geçmiş iletişim kutusu açıkken eklenen yeni öğeleri görebilmek için kullanılır.
* Kapat Alt+K, Escape veya Alt+F4: Geçmiş iletişim kutusunu kapatır.  

Listedeyken ENTER tuşuna basarsak, odaktaki giriş, geçmiş iletişim kutusunun arkasındaki uygulamaya kopyalanacaktır.  

Örneğin, not defterimiz açıksa, geçmişi açarsak ve ilk girişte ENTER'a basarsak, seçilen öğeyi not defterine kopyalayacaktır.  

## zPano'nun sınırlamaları:  

zPano, Fake Clipboard veya Clipspeak gibi aynı işlevi gerçekleştiren diğer eklentilerle uyumlu değildir. Bu eklentiler yüklüyse ve zPano kullanılmak isteniyorsa, iki eklentinin de devre dışı bırakılması gerekir.  

NVDA'yı yeniden başlattığımızda geçmiş girişlerinin silineceğini unutmayın.  

zPano geçmişini kullanırsak, Windows pano geçmişinde yinelenen girişler olabilir. Hangisini kullanmak istersek seçmemiz gerekir.  

## teşekkürler:  

* Javi Domínguez: Özverili yardımları ve pano izleme işlevine katkıda bulunduğu için.
* Portekizce Brezilya: pedro-hdias
* Rusça: Valentin Kupriyanov
* Türkçe: Umut KORKMAZ

# Sürüm Geçmişi:

## Sürüm 0.4.

* Oyun modu eklendi.

Bu modu etkinleştirmek için, girdi Hareketleri penceresinde bir hareket atamamız gerekir.  

Bu mod, panoya kopyalanan ve çeviriye ihtiyaç duyan oyunlar için iyi çalışır.  

Eklenti seçeneklerinde, pano güncellemesinin yenileme hızını artırma ve çevirinin hedef dilini seçme olanağına sahip olacağız.  

Bu durumda oyunun kaynak dili otomatik olarak algılanacak ve panoya kopyalananlar seçtiğimiz dile çevrilecektir.  

Oyun modu etkinleştirilirken, pano geçmişi de dahil olmak üzere eklentinin geri kalan tüm komutları devre dışı bırakılır.  

## Sürüm 0.3.1.

* Eklentinin güvenli ekranlarda çalışmasını önlemek için güncelleme yapıldı.
* Arapça dil eklendi.

## Sürüm 0.3:

* Kopyalama sırasında metin seçilirse algılama eklendi.

Artık kopyaladığımızda metin algılamıyorsa eklenti bize bir mesaj ile bildirecektir.  

* Pano ile ilgili eklenti işlevlerini hızlı bir şekilde devre dışı bırakabilme ve etkinleştirebilme özelliği eklendi.

Girdi hareketlerinde, panoya atıfta bulunulanları hızlı bir şekilde etkinleştirmek ve devre dışı bırakmak için bir kombinasyon yapılandırabiliriz.  

Panoyu devre dışı bıraktığımızda mesajlar, NVDA'nın pano için önceden tanımladığı mesajlarla birlikte Windows'un yerel mesajları olacaktır.  

Bu, aktif olduğu takdirde etkin olan geçmişi etkilemeyecektir.  

* Kiril karakterlerini kullanan klavyeler için destek eklendi.

Kiril karakterlerini kullanan klavye düzenlerindeki bir sorun düzeltildi.  

* Rusça, Türkçe ve Portekizce Brezilya dilleri eklendi.

## Sürüm 0.2:

* Tüm pano işlevleri cTypes olarak değiştirildi.
* Artık pano, NVDA ve wxpython işlevlerini kullanmaktan kaçınarak sistem işlevleriyle doğrudan ele alınacaktır.
* Eklenti çevrilmeye hazır hale getirildi.

## Sürüm 0.1.5:

* Panoya kopyalananları ve Geçmişe eklenenleri duyrur.

Eklenti seçeneklerinde Pano geçmişini aç seçeneğini etkinleştirdiysek, bir seçeneğe daha sahibiz.

Bu seçenek ile geçmişe ne kopyalanırsa sesçendirilecektir.  

Sadece son kopyalanan diziden bahsedilecek ve kopyalanan başka bir dizi tekrar söyleninceye kadar tekrarlanmayacaktır.

* Eklentiyi ilk kez başlattığınızda pano temizlenecektir.

Artık NVDA'yı başlattığımızda panoda bulunanları kopyalamayacak, pano boş olacak.  

Bu, Windows pano geçmişini etkilemez.  

*** Uyarı: Panoda sahip olduğumuz önemli bir şeyin silinebileceğinden bunu dikkate almalıyız. ***

## Sürüm 0.1.4:

* Pano verilerini alma şekli değiştirildi.

## Sürüm 0.1.3:

* Kullanılacak minimum sürüm olarak NVDA 2021.2'ye eklenti gereksinimi yüklendi.
* Geçmiş için seçenekler eklendi.
* Artık geçmişe bir şey kopyalandığında ses istiyormuş gibi izleme süresini seçebiliriz.
* Pano anahtarlarını duyurmamak için Word ve Excel desteği eklendi.
* Pano artık izleniyor, böylece panoya kopyalayan herhangi bir eklenti artık destekleniyor, hatta NVDA'dan odaklanmaya kopyalama bile.

## Sürüm 0.1.2:

* Seçeneklerde pano sesli duyurularını etkinleştir veya devre dışı bırak eklendi.
* İzin verilen uygulamalarda pano tuşlarına karşılık gelen mesajları atlayacaktır.

## Sürüm 0.1.1:

* Pano yakalamaları ve bunların yönetme şekli değiştirildi.
* Panoyu açık bırakan hata düzeltildi.

## Sürüm 0.1:

* İlk Sürüm.
