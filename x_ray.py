import gvxrPython3 as gvxr
import Spectrum
import cv2 as cv
import numpy as np
from PIL import Image


# This script uses GVirtualXRay created by Dr Franck P. Vidal
# Copyright (c) 2019, Dr Franck P. Vidal (franck.p.vidal@fpvidal.net), http://www.fpvidal.net/
# All rights reserved.

# This script is created by Jones Jernfors
# Copyright (c) 2022, Jones Jernfors (jones.jernfors@outlook.com)
# All rights reserved.

# This script is where the x-ray parameters are set and x-ray image is calculated


def calculate_xray(detector_coords, detector_pixels, tube_distance, kvp, mas, trans, tube_height, filter_z, filter_rho,
                   filter_thickness, filter_z2, filter_rho2, filter_thickness2):

    # Transformation matrices, note that all the matrices are the same
    if trans == "AP":
        gvxr.setLocalTransformationMatrix("skeleton", (4.408728735481053e-17, -0.7200000286102295, 0.0, 0.0,
                                                       0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0,
                                                       0.0, 0.0, 0.7200000286102295, 0.0, 0.0, 0.0, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("liver", (4.408728735481053e-17, -0.7200000286102295, 0.0, 0.0,
                                                    0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0, 0.0, 0.0,
                                                    0.7200000286102295, 0.0, 0.0, 0.0, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("lungs", (4.408728735481053e-17, -0.7200000286102295, 0.0, 0.0,
                                                    0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0,
                                                    0.0, 0.0, 0.7200000286102295, 0.0, 0.0, 0.0, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("lung vessels", (4.408728735481053e-17, -0.7200000286102295, 0.0, 0.0,
                                                           0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0,
                                                           0.0, 0.0, 0.7200000286102295, 0.0, 0.0, 0.0, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("kidneys", (4.408728735481053e-17, -0.7200000286102295, 0.0, 0.0,
                                                      0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0,
                                                      0.0, 0.0, 0.7200000286102295, 0.0, 0.0, 0.0, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("stomach", (4.408728735481053e-17, -0.7200000286102295, 0.0, 0.0,
                                                      0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0,
                                                      0.0, 0.0, 0.7200000286102295, 0.0, 0.0, 0.0, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("thorax", (4.408728735481053e-17, -0.7200000286102295, 0.0, 0.0,
                                                     0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0,
                                                     0.0, 0.0, 0.7200000286102295, 0.0, 0.0, 0.0, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("head", (4.408728735481053e-17, -0.7200000286102295, 0.0, 0.0,
                                                   0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0,
                                                   0.0, 0.0, 0.7200000286102295, 0.0, 0.0, 0.0, 0.0, 1.0))
    elif trans == "PA":
        gvxr.setLocalTransformationMatrix("skeleton", (4.408728735481053e-17, 0.7200000286102295, 0.0, 0.0,
                                                       -0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0, 0.0, 0.0,
                                                       0.7200000286102295, 0.0, -216.00001525878906,
                                                       1.3226186537315405e-14, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("liver", (4.408728735481053e-17, 0.7200000286102295, 0.0, 0.0,
                                                    -0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0, 0.0, 0.0,
                                                    0.7200000286102295, 0.0, -216.00001525878906,
                                                    1.3226186537315405e-14, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("lungs", (4.408728735481053e-17, 0.7200000286102295, 0.0, 0.0,
                                                    -0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0, 0.0, 0.0,
                                                    0.7200000286102295, 0.0, -216.00001525878906,
                                                    1.3226186537315405e-14, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("lung vessels", (4.408728735481053e-17, 0.7200000286102295, 0.0, 0.0,
                                                           -0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0, 0.0,
                                                           0.0,
                                                           0.7200000286102295, 0.0, -216.00001525878906,
                                                           1.3226186537315405e-14, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("kidneys", (4.408728735481053e-17, 0.7200000286102295, 0.0, 0.0,
                                                      -0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0, 0.0, 0.0,
                                                      0.7200000286102295, 0.0, -216.00001525878906,
                                                      1.3226186537315405e-14, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("stomach", (4.408728735481053e-17, 0.7200000286102295, 0.0, 0.0,
                                                      -0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0, 0.0, 0.0,
                                                      0.7200000286102295, 0.0, -216.00001525878906,
                                                      1.3226186537315405e-14, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("thorax", (4.408728735481053e-17, 0.7200000286102295, 0.0, 0.0,
                                                     -0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0, 0.0, 0.0,
                                                     0.7200000286102295, 0.0, -216.00001525878906,
                                                     1.3226186537315405e-14, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("head", (4.408728735481053e-17, 0.7200000286102295, 0.0, 0.0,
                                                   -0.7200000286102295, 4.408728735481053e-17, 0.0, 0.0, 0.0, 0.0,
                                                   0.7200000286102295, 0.0, -216.00001525878906,
                                                   1.3226186537315405e-14, 0.0, 1.0))
    elif trans == "LAT_left":
        detector_coords = -detector_coords[0] + 2, detector_coords[1] + 1.2
        gvxr.setLocalTransformationMatrix("skeleton", (-0.7200000286102295, -8.817457470962107e-17, 0.0, 0.0,
                                                       8.817457470962107e-17, -0.7200000286102295, 0.0,
                                                       0.0, 0.0, 0.0, 0.7200000286102295, 0.0, -144.0,
                                                       -93.60000610351562, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("liver", (-0.7200000286102295, -8.817457470962107e-17, 0.0, 0.0,
                                                    8.817457470962107e-17, -0.7200000286102295, 0.0,
                                                    0.0, 0.0, 0.0, 0.7200000286102295, 0.0, -144.0,
                                                    -93.60000610351562, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("lungs", (-0.7200000286102295, -8.817457470962107e-17, 0.0, 0.0,
                                                    8.817457470962107e-17, -0.7200000286102295, 0.0,
                                                    0.0, 0.0, 0.0, 0.7200000286102295, 0.0, -144.0,
                                                    -93.60000610351562, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("lung vessels", (-0.7200000286102295, -8.817457470962107e-17, 0.0, 0.0,
                                                           8.817457470962107e-17, -0.7200000286102295, 0.0,
                                                           0.0, 0.0, 0.0, 0.7200000286102295, 0.0, -144.0,
                                                           -93.60000610351562, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("kidneys", (-0.7200000286102295, -8.817457470962107e-17, 0.0, 0.0,
                                                      8.817457470962107e-17, -0.7200000286102295, 0.0,
                                                      0.0, 0.0, 0.0, 0.7200000286102295, 0.0, -144.0,
                                                      -93.60000610351562, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("thorax", (-0.7200000286102295, -8.817457470962107e-17, 0.0, 0.0,
                                                     8.817457470962107e-17, -0.7200000286102295, 0.0,
                                                     0.0, 0.0, 0.0, 0.7200000286102295, 0.0, -144.0,
                                                     -93.60000610351562, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("stomach", (-0.7200000286102295, -8.817457470962107e-17, 0.0, 0.0,
                                                      8.817457470962107e-17, -0.7200000286102295, 0.0,
                                                      0.0, 0.0, 0.0, 0.7200000286102295, 0.0, -144.0,
                                                      -93.60000610351562, 0.0, 1.0))
        gvxr.setLocalTransformationMatrix("head", (-0.7200000286102295, -8.817457470962107e-17, 0.0, 0.0,
                                                   8.817457470962107e-17, -0.7200000286102295, 0.0,
                                                   0.0, 0.0, 0.0, 0.7200000286102295, 0.0, -144.0,
                                                   -93.60000610351562, 0.0, 1.0))

    # Set up the detector
    gvxr.setDetectorPosition(0, detector_coords[0], detector_coords[1], "cm")
    gvxr.setDetectorUpVector(0, 0, -1)
    gvxr.setDetectorNumberOfPixels(detector_pixels[0], detector_pixels[1])
    gvxr.setDetectorPixelSize(0.5, 0.5, "mm")

    # Function for the x ray spectrum
    [specKvp, specInt, dose_coefficient] = Spectrum.spectrum(kvp, mas, filter_z, filter_rho, filter_thickness,
                                                             filter_z2, filter_rho2, filter_thickness2)
    # Source position and type
    gvxr.setSourcePosition(-tube_distance, 0, tube_height, "cm")
    gvxr.usePointSource()
    # Adding kV energies into the spectrum
    # The constant 500 could be modified into variable, which would change according to kvp and mas
    # This would enhance brightness in high kvp imaging, which is now rather dim
    for i in range(len(specInt)):
        gvxr.addEnergyBinToSpectrum(specKvp[i], "keV", specInt[i]*500)

    # Compute an X-ray image
    gvxr.disableArtefactFiltering()
    x_ray_image = np.array(gvxr.computeXRayImage())

    # Resize the image into (2874,2840), as seen in dicom data
    x_ray_image = cv.resize(x_ray_image, dsize=(2840, 2874), interpolation=cv.INTER_CUBIC)

    # Dose calculation
    d00 = 0.1405
    d10 = -0.004523
    d01 = -0.002116
    d20 = 4.724e-05
    d11 = -8.032e-05
    d02 = 3.523e-05
    d30 = -1.619e-07
    d21 = 2.647e-06
    d12 = -5.169e-07

    # Absorbed dose (mGy)
    Dose = d00 + d10 * kvp + d01 * mas + d20 * kvp ** 2 + d11 * kvp * mas + d02 * mas ** 2 + d30 * kvp ** 3 + d21 * \
           kvp ** 2 * mas + d12 * kvp * mas ** 2
    # Here we take the tube distance into account in dose
    # The test images were taken within 138,7 cm distance, so first we get the non-attenuated dose
    # and then we divide with distance squared
    Dose = float(Dose) * float(dose_coefficient) * 1.387**2
    Dose = Dose / (tube_distance / 100)**2


    # DAP = mGy * cm2
    # 0.05**2 is the height/width pixel spacing and 2.723 is a calculated coefficient
    Area = (detector_pixels[0] * detector_pixels[1] * 0.05 ** 2) * 2.723
    DAP = Dose * Area
    DAP = float("{:.1f}".format(DAP))

    # SNR calculation
    p00 = -515.8
    p10 = 12.36
    p01 = 51.9
    p20 = -0.05641
    p11 = -0.4718
    p02 = 12.05
    p21 = 0.0004108
    p12 = -0.3407
    p03 = -0.01473
    p22 = 0.002294
    p13 = 0.0003084
    p04 = -2.736 * 10 ** -5

    SNR = p00 + p10 * kvp + p01 * mas + p20 * kvp ** 2 + p11 * kvp * mas + p02 * mas ** 2 + p21 * kvp ** 2 * mas + \
          p12 * kvp * mas ** 2 + p03 * mas ** 3 + \
          p22 * kvp ** 2 * mas ** 2 + p13 * kvp * mas ** 3 + p04 * mas ** 4

    # Noise calculation
    b00 = 9.601 * 10 ** 4
    b10 = 57.04
    b01 = -3288
    b20 = 0.02065
    b11 = -1.21
    b02 = 36.47
    b21 = 0.0003788
    b12 = 0.00614
    b03 = -0.1308

    NoiseValue = b00 + b10 * SNR + b01 * kvp + b20 * SNR ** 2 + b11 * SNR * kvp + b02 * kvp ** 2 + b21 * SNR ** 2 * \
                 kvp + b12 * SNR * kvp ** 2 + \
                 b03 * kvp ** 3

    # Produce noisy image
    # If x_ray_image isn't in abs, it may produce errors due to values being negative
    noisy = np.random.poisson(abs(x_ray_image) / np.amax(x_ray_image) * NoiseValue) / NoiseValue * np.amax(x_ray_image)

    # Log scale equalization
    c = 65535 / np.log(1 + np.max(noisy))
    log_image = c * (np.log(noisy + 1))
    log_image = np.amax(log_image) - log_image

    kuva = Image.fromarray(np.int16(log_image), 'I;16')

    # Transpose the image so stuff is correct side
    horz_img = kuva.transpose(method=Image.FLIP_LEFT_RIGHT)

    if trans == "PA":
        kuva.save("Images/x_ray_image.png")
    else:
        horz_img.save("Images/x_ray_image.png")
    gvxr.resetBeamSpectrum()

    return DAP
