# reference: Tutorial_Fits_file_2023 from TA
import numpy as np
import matplotlib.pyplot as plt

from astropy.io import fits  #import fits file
hdu = fits.open('example.fits')

img = hdu[0].data
plt.hist(img.flatten(), bins=1000)   #使用 img.flatten() 將二維數據拉成一維
plt.xlabel('Brightness')
plt.ylabel('Number of Pixels')
plt.xlim([40, 110])
plt.show()

from photutils.segmentation import detect_sources
# 製作一個遮罩，source 的篩選條件為至少 5 個連續 pixel 且高於背景雜訊 3 倍
# 此處使用 np.median(img) 來當作背景雜訊值，差距不會太大
segment_map = detect_sources(img, threshold= 3*np.median(img),npixels= 5)
mask = segment_map.make_source_mask()
masked_img = img_copy   # 複製一份 img 到 masked_img 這個變數
masked_img = np.nan  # 將 mask 的 pixel 數值改成 NaN (Not a Number)

uncertainty_mean_background = np.nanstd(masked_img) / np.sqrt(np.nansum(masked_img))
print('Mean of Mask_img:' ,np.nanmean(masked_img) , "\n" 'Uncertainty of Mask_img:', uncertainty_mean_background)
##########
Mean of Mask_img: 63.703323 
Uncertainty of Mask_img: 0.0021849032


