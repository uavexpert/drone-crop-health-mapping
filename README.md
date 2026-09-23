# Drone Crop-Health Mapping

Mapping crop health with an affordable consumer drone (DJI Mini 3): RGB-based vegetation indices (VARI/ExG) processed with open-source tools (WebODM, QGIS).

## 00 — Pipeline test (Sep 2026)

Before flying over real crops, I validated the full workflow on a practice field:

- **Flight:** DJI Mini 3, automated grid mission with Litchi Pilot (45 m AGL, 75% front / 70% side overlap, nadir camera, locked manual exposure)
- **Processing:** WebODM (fast orthophoto) — 35 images stitched into one orthomosaic
- **Analysis:** QGIS Raster Calculator — VARI vegetation index map
- **Result:** complete orthomosaic with no gaps; VARI map uniform, as expected on bare soil

## 01 — Winter wheat (upcoming)

Two repeat flights over the same winter wheat parcel:

1. Autumn 2026 — tillering (BBCH 20–29)
2. Spring 2027 — stem elongation to heading (BBCH 30–59)

Planned outputs: orthomosaic, VARI/ExG vigor maps, and a change map between the two dates.

*Note: the Mini 3 has no NIR sensor, so VARI/ExG are RGB-based proxies — not true NDVI.*
