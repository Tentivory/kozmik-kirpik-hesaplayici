#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KOZMİK KİRPİK HESAPLAYICI v0.001
Bu program, kuantum fiziği, astroloji ve çay demleme sanatını birleştirerek
bugün kaç kere göz kırpmamanız gerektiğini hesaplar.

UYARI: Bu hesaplama %100 doğrudur. Bilim adamları onayladı. (Kendileri.)
"""

import random
import time

def hesapla_kirpik(isim):
    print(f"\nSayın {isim}, kozmik hesaplamalar başlıyor...")
    print("Evrenle bağlantı kuruluyor...")
    time.sleep(1.5)
    print("Kara delikler sorgulanıyor...")
    time.sleep(1)
    print("Kedi tüyü sayısı hesaplanıyor...")
    time.sleep(0.8)
    
    temel = len(isim) * 42  # 42 her şeyin cevabıdır
    rastgele = random.randint(100, 9999)
    kirpik = temel + rastgele + int(time.time()) % 777
    
    # Gizli not: bazen sistemler de göz kırpmak ister
    print(f"\n✨ SONUÇ: Bugün tam olarak {kirpik} kere göz kırpmalısın.")
    print("Bu sayıyı tutmazsan evren kısılır. Sorumluluk sende.")
    print("\nİyi göz kırpmalar! (Ama abartma, gözün kurumasın.)")

if __name__ == "__main__":
    print("=" * 50)
    print("   KOZMİK KİRPİK HESAPLAYICI")
    print("   (Bilimsel Görünen Ama Değil)")
    print("=" * 50)
    isim = input("\nAdını gir (kozmik işlem için): ").strip()
    if not isim:
        isim = "Adsız Kozmonot"
    hesapla_kirpik(isim)
    
    print("\n" + "-" * 40)
    print("DAMGA: Grok'un Saçma Mührü 🔐")
    print("İMZA: Kayyum Grok (Resmi Değil)")
    print("TARİH: 07.11.2026")
    print("İSİM: Tentivory'nin Absürt Dehası")
    print("-" * 40)
