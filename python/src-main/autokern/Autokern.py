'''
robofont-extensions-and-scripts
Autokern.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com

Apache License

Version 2.0, January 2004

http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

"License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.

"Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.

"Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.

"You" (or "Your") shall mean an individual or Legal Entity exercising permissions granted by this License.

"Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files.

"Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.

"Work" shall mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below).

"Derivative Works" shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof.

"Contribution" shall mean any work of authorship, including the original version of the Work and any modifications or additions to that Work or Derivative Works thereof, that is intentionally submitted to Licensor for inclusion in the Work by the copyright owner or by an individual or Legal Entity authorized to submit on behalf of the copyright owner. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to the Licensor or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Licensor for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by the copyright owner as "Not a Contribution."

"Contributor" shall mean Licensor and any individual or Legal Entity on behalf of whom a Contribution has been received by Licensor and subsequently incorporated within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.

3. Grant of Patent License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted. If You institute patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.

4. Redistribution. You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:

You must give any other recipients of the Work or Derivative Works a copy of this License; and

You must cause any modified files to carry prominent notices stating that You changed the files; and

You must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work, excluding those notices that do not pertain to any part of the Derivative Works; and

If the Work includes a "NOTICE" text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file, excluding those notices that do not pertain to any part of the Derivative Works, in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, within a display generated by the Derivative Works, if and wherever such third-party notices normally appear. The contents of the NOTICE file are for informational purposes only and do not modify the License. You may add Your own attribution notices within Derivative Works that You distribute, alongside or as an addendum to the NOTICE text from the Work, provided that such additional attribution notices cannot be construed as modifying the License. You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License.

5. Submission of Contributions. Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.

6. Trademarks. This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file.

7. Disclaimer of Warranty. Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

8. Limitation of Liability. In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.

9. Accepting Warranty or Additional Liability. While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations and/or rights consistent with this License. However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS
'''


import os
import shutil
import math
import time

from tfs.common.TFSFont import *
from AutokernSettings import AutokernSettings
#from tfs.common.TFSSilhouette import *
from tfs.common.TFTiming import TFTiming
from tfs.common.TFSMap import TFSMap
import tfs.common.TFSMath as TFSMath
from tfs.common.TFSPath import minmaxPaths, minmaxMerge, openPathWithPoints
from tfs.common.TFSPoint import TFSPoint
#from collections import defaultdict


TFSMath.setFloatRoundingTolerance(0.1)
TFSMath.setDefaultPrecisionDigits(1)

def formatGlyphUnicode(glyph):
    if glyph.unicode is None:
        return 'None'
    else:
        return u'%d %s' % ( glyph.unicode,
                                 hex(glyph.unicode), )

def formatUnicode(value):
    if value is None:
        return 'None'
    else:
        return '0x%X' % ( value, )

def formatGlyphName(glyph):
    if glyph.unicode is None:
        name = glyph.name
    elif glyph.name == unichr(glyph.unicode):
        name = glyph.name
    else:
        name = u'%s &#%d;' % ( glyph.name,
                               glyph.unicode, )
    return u'%s (%s)' % ( name,
                          formatGlyphUnicode(glyph), )

def getCachedMinmax(contours):
    return minmaxPaths(contours)

class Autokern(TFSMap):

    def __init__(self):
        TFSMap.__init__(self)

    def isCombiningGlyph(self, glyph):
        names = ('dieresis_acutecomb',
                 'dieresis_gravecomb',
                 'hungarumlaut',
                'ring',
                'dotaccent',

                 'dieresistonos',

                'acutecomb',
                'dotbelowcomb',
                'gravecomb',
                'hookabovecomb',
                'tildecomb',

                'acute',
                'base',
                'breve',
                'caron',
                'cedilla',
                'circumflex',
                'comma below',
                'corner leftwards',
                'diaeresis',
                'dialytika',
                'dialytika and tonos',
                'dot above',
                'double acute',
                'grave',
                'hamza above',
                'hamza below',
                'hook',
                'hook symbol',
                'horn',
                'macron',
                'madda above',
                'middle dot',
                'ogonek',
                'rays',
                'ring above',
                'ring above and acute',
                'stroke',
                'stroke and acute',
                'tilde',
                'tonos',
                'upturn',

                 )
        if glyph.name in names:
            return True
        '''
        Look for variations like 'breve.cap' or 'breve.cyr'.
        '''
        if '.' in glyph.name[1:]:
            shortName = glyph.name[:glyph.name.index('.')]
            if shortName in names:
                return True
        return False

    def subrenderGlyphContours(self, tfsSvg, contours, strokeColor):
        from tfs.common.TFSSvg import TFSSvgPath
        ON_POINT_COLOR = 0x7f7f7f7f
        CONTROL_POINT_COLOR = 0x7fafafaf
        for contour in contours:
            tfsSvg.addItem(TFSSvgPath(contour).addStroke(strokeColor, 2).addPointHighlights(ON_POINT_COLOR, CONTROL_POINT_COLOR))


    def renderSvgScene(self,
                       filename,
                       pathTuples,
                       hGuidelines=None):
        from tfs.common.TFSSvg import TFSSvg, TFSSvgPath
        if filename is None:
            dstFile = filename
        else:
            filename = '%s.svg' % ( filename, )
            dstFile = os.path.abspath(os.path.join(self.svg_folder, filename))

        CANVAS_BACKGROUND_COLOR = 0xffffffff
        CANVAS_BORDER_COLOR = 0x07fbfbfbf
        tfsSvg = TFSSvg().withBackground(CANVAS_BACKGROUND_COLOR).withBorder(CANVAS_BORDER_COLOR)

    #    if pathTuples:
        for color, contours in pathTuples:
            self.subrenderGlyphContours(tfsSvg, contours, color)

        if hGuidelines:
            for hGuideline in hGuidelines:
                p0 = TFSPoint(hGuideline, self.dstUfoFont.info.descender)
                p1 = TFSPoint(hGuideline, self.dstUfoFont.info.ascender)
                GUIDELINE_COLOR = 0x7fdfdfdf
                tfsSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))

        vGuidelines = ( 0,
                        self.dstUfoFont.info.ascender,
                        self.dstUfoFont.info.descender,
                        )
        if vGuidelines:
            minmax = None
            for color, contours in pathTuples:
                minmax = minmaxMerge(minmax, minmaxPaths(contours))

            for vGuideline in vGuidelines:
                p0 = TFSPoint(0, vGuideline)
                p1 = TFSPoint(minmax.maxX, vGuideline)
                GUIDELINE_COLOR = 0x7fdfdfdf
                tfsSvg.addItem(TFSSvgPath(openPathWithPoints(p0, p1)).addStroke(GUIDELINE_COLOR, 1))

        SVG_HEIGHT = 400
        SVG_MAX_WIDTH = 800
        self.timing.mark('renderSvgScene.0')
        svgdata = tfsSvg.renderToFile(dstFile, margin=10, height=SVG_HEIGHT, maxWidth=SVG_MAX_WIDTH, timing=self.timing)
        self.timing.mark('renderSvgScene.1')
        if filename is not None:
            return filename
        else:
            return svgdata


    def processKerningPair_flate(self, ufoglyph0, ufoglyph1):

        renderLog = self.log_dst is not None

        contours0 = ufoglyph0.getContours()
        contours1 = ufoglyph1.getContours()
        minmax0 = minmaxPaths(contours0)
        minmax1 = minmaxPaths(contours1)
        naiveSpacing = minmax0.maxX - minmax1.minX

        minSpacing = 0


    #    import time
    #    time0 = time.time()
        debugPaths('contours1', contours1)
        contours1_plusMin = inflatePaths(contours1, self.min_distance)
        debugPaths('contours1_plusMin', contours1_plusMin)

    #    time1 = time.time()
    #    print 'inflatePathsLeft', time1 - time0
    #    time0 = time1
        SILHOUETTE_RESOLUTION = 2.0
        minDistanceSpacing = findSilhouetteContactSpacing(contours0, contours1_plusMin, SILHOUETTE_RESOLUTION)
    #    time1 = time.time()
    #    print 'findSilhouetteContactSpacing', time1 - time0
    #    time0 = time1
    ##    minSpacing = kerning.min_distance + findSilhouetteContactSpacing(contours0, contours1_plusMin, SILHOUETTE_RESOLUTION)

        contours0_midRounding = deflatePaths(contours1, self.rounding)
        debugPaths('contours0_midRounding', contours0_midRounding)
        contours0_afterRounding = inflatePaths(contours0_midRounding, self.rounding)
        debugPaths('contours0_afterRounding', contours0_afterRounding)
        roundingSpacing = findSilhouetteContactSpacing(contours0_afterRounding, contours1_plusMin, SILHOUETTE_RESOLUTION)
    #
    #    contours1_plusMin = inflatePathsLeft(contours1, kerning.min_distance)
    #    contours = FSilhouette.deflatePaths(contours, capHeight * 0.05)
    #    time1 = time.time()
    #    print ''

        print 'minDistanceSpacing', minDistanceSpacing
        debugPaths('contours0', contours0)
        debugPaths('contours1_plusMin', contours1_plusMin)

        if renderLog:
#            from tfs.common.TFSSvg import *
            filenamePrefix = 'tfs-%s-%s' % ( chr(ufoglyph0.unicode),
                                             chr(ufoglyph1.unicode), )
            phase = 1

    #        for contour in contours1:
    #            print 'contour', type(contour), contour.description()

            naiveSpacingSvg = self.renderSvgScene(
                                                  filenamePrefix + '-naive-spacing',
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(naiveSpacing, 0)) for contour in contours1], ),
                                                           ),
                                             hGuidelines = ( naiveSpacing, ) )
            phase += 1
            minDistanceSpacingSvg = self.renderSvgScene(
                                                        filenamePrefix + '-min-spacing',
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(minDistanceSpacing, 0)) for contour in contours1], ),
                                                           ( 0x7fafafff, [contour.applyPlus(TFSPoint(minDistanceSpacing, 0)) for contour in contours1_plusMin], ),
                                                           ),
                                             hGuidelines = ( naiveSpacing, ) )
            phase += 1
            roundingSpacingSvg = self.renderSvgScene(
                                                     filenamePrefix + '-rounding',
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7fafffaf, contours0_midRounding, ),
                                                           ( 0x7fafffaf, contours0_afterRounding, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(roundingSpacing, 0)) for contour in contours1], ),
                                                           ( 0x7fafafff, [contour.applyPlus(TFSPoint(roundingSpacing, 0)) for contour in contours1_plusMin], ),
                                                           ),
                                             hGuidelines = ( naiveSpacing, ) )
            phase += 1

            import tfs.common.TFSProject as TFSProject
            mustache_template_file = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'log_kerning_pair_html_mustache.txt'))
            with open(mustache_template_file, 'rt') as f:
                mustache_template = f.read()

            pageTitle = u'pyautokern Log: Kerning %s vs. %s' % ( formatGlyphName(ufoglyph0),
                                                                 formatGlyphName(ufoglyph1), )

            def formatEmScalar(value):
                return '%0.3f em' % (value / float(self.units_per_em))

            def formatGlyphMap(glyph, glyphMinmax):
                return {
                           'glyphName': formatGlyphName(glyph),
                           'minX': formatEmScalar(glyphMinmax.minX),
                           'maxX': formatEmScalar(glyphMinmax.maxX),
                           'minY': formatEmScalar(glyphMinmax.minY),
                           'maxY': formatEmScalar(glyphMinmax.maxY),
                        }

            mustacheMap = {
                           'pageTitle': pageTitle,
                           'minmax0': minmax0,
                           'minmax1': minmax1,
                           'naiveSpacing': formatEmScalar(naiveSpacing),
                           'minDistanceSpacing': formatEmScalar(minDistanceSpacing),
                           'roundingSpacing': formatEmScalar(roundingSpacing),
                           'min_distance': formatEmScalar(self.min_distance),
                           'max_distance': formatEmScalar(self.max_distance),
                           'rounding': formatEmScalar(self.rounding),

                           'naiveSpacingSvg': naiveSpacingSvg,
                           'minSpacingSvg': minDistanceSpacingSvg,
                           'roundingSpacingSvg': roundingSpacingSvg,

                           'glyph0': formatGlyphName(ufoglyph0),
                           'glyph1': formatGlyphName(ufoglyph1),

                           'glyphMaps': ( formatGlyphMap(ufoglyph0, minmax0),
                                          formatGlyphMap(ufoglyph1, minmax1),
                                          )
                           }

            for key in ( 'ascender',
                         'descender',
                        ):
                mustacheMap[key] = formatEmScalar(getattr(self.dstUfoFont.info, key))

            for key in (
                         'unitsPerEm',
                         'familyName',
                         'styleName',
                         'fullName',
                         'fontName',
                        ):
                mustacheMap[key] = getattr(self.dstUfoFont.info, key)

            import pystache
            logHtml = pystache.render(mustache_template, mustacheMap)

            logFilename = '%s.html' % ( filenamePrefix, )
            logFile = os.path.abspath(os.path.join(self.html_folder, logFilename))
            with open(logFile, 'wt') as f:
                # TODO: explicitly encode unicode
                f.write(logHtml)


    def getSrcGlyphContours(self, ufoglyph):
#        ufoglyph = self.srcUfoFont.getGlyphByName(ufoglyph.name)
#        if ufoglyph is None:
#            return None
        if ufoglyph.unicode in self.srcContoursCache:
            return self.srcContoursCache[ufoglyph.unicode]
        contours = ufoglyph.getContours()
        self.srcContoursCache[ufoglyph.unicode] = contours
        return contours


    def getGlyphContours(self, ufoglyph):
        if ufoglyph.name in self.dstContoursCache:
            return self.dstContoursCache[ufoglyph.name]
        contours = ufoglyph.getContours()
        self.dstContoursCache[ufoglyph.name] = contours
        return contours


    def getGlyphPixels(self, ufoglyph):
        if ufoglyph.name in self.pixelsCache:
            return self.pixelsCache[ufoglyph.name]
        RASTERIZE_CELL_SIZE = self.precision
        pixels = self.rasterizeGlyph(ufoglyph, RASTERIZE_CELL_SIZE)
        if pixels is not None:
            pixels = self.padPixels(pixels, self.convertToPixelUnits(self.max_distance, RASTERIZE_CELL_SIZE))
        self.pixelsCache[ufoglyph.name] = pixels
        return pixels


    def dumpPixelBlock(self, name, pixels):
        if not pixels:
            print name, '[No pixels]'
            return
        print name, len(pixels), 'pixel rows'
        for row in pixels:
            buffer = []
            for pixel in row:
                buffer.append('1' if pixel else '0')
            print '\t', ''.join(buffer)
        print


    def padPixels(self, pixels, padding):
        hPadding = (False,) * padding
        rowLength = len(pixels[0]) + 2 * padding
        vPadding = (False,) * rowLength
        result = []
        for _ in xrange(padding):
            result.append(vPadding)
        for row in pixels:
            result.append(hPadding + tuple(row) + hPadding)
        for _ in xrange(padding):
            result.append(vPadding)
        return result

    def convertToPixelUnits(self, value, RASTERIZE_CELL_SIZE):
        return int(math.ceil(value / float(RASTERIZE_CELL_SIZE)))

    def inflatePixelBlock(self, pixels, radius, RASTERIZE_CELL_SIZE):
#        radius = 100

        maskScale = self.convertToPixelUnits(radius, RASTERIZE_CELL_SIZE)
        maskSize = 1 + 2 * maskScale
        mask = []
        for y in xrange(maskSize):
            maskRow = []
            for x in xrange(maskSize):
                xOffset = x - maskScale
                yOffset = y - maskScale
                xDiff = xOffset * RASTERIZE_CELL_SIZE
                yDiff = yOffset * RASTERIZE_CELL_SIZE
                maskValue = (radius * radius) > (xDiff * xDiff) + (yDiff * yDiff)
#                xDiff = x * RASTERIZE_CELL_SIZE - radius
#                yDiff = y * RASTERIZE_CELL_SIZE - radius
#                maskValue = (radius * radius) > (xDiff * xDiff) + (yDiff * yDiff)
#                print 'x', x, 'y', y, 'radius', radius, 'xDiff', xDiff, 'yDiff', yDiff, 'maskValue', maskValue
                maskRow.append(maskValue)
            mask.append(maskRow)



        result = []
        for row in pixels:
            result.append(list(row))

#        result = []
        for y1, row1 in enumerate(pixels):
            for x1, pixel1 in enumerate(row1):
                if not pixel1:
                    continue
                # Inflate pixel
                for y2, row2 in enumerate(mask):
                    for x2, pixel2 in enumerate(row2):
                        if not pixel2:
                            continue
                        x = x1 + x2 - maskScale
                        y = y1 + y2 - maskScale
                        if 0 <= y < len(result):
                            if 0 <= x < len(result[y]):
                                result[y][x] = True

        return result


    def rasterizeGlyph(self, ufoglyph, RASTERIZE_CELL_SIZE):
        if ufoglyph.unicode in self.rasterCache:
            return self.rasterCache[ufoglyph.unicode]
        pixels = ufoglyph.rasterize(cellSize=RASTERIZE_CELL_SIZE,
                                   xMin=self.minmax.minX,
                                   yMin=self.minmax.minY,
                                   xMax=self.minmax.maxX,
                                   yMax=self.minmax.maxY)
        self.rasterCache[ufoglyph.unicode] = pixels
        return pixels

#    def findMinAdvance(self, pixels0, pixels1, tolerancePixels=0):
    def findMinAdvance(self, pixels0, pixels1, intrusionTolerancePixels=0, minNonIntrusionCount=0):
        if len(pixels0) != len(pixels1):
            raise Exception('pixel heights do not match. %d != %d', len(pixels0), len(pixels1))

        def leftRowProfile(row):
            for index, pixel in enumerate(row):
                if pixel:
                    return index
            return None

        def rightRowProfile(row):
            for index, pixel in enumerate(reversed(row)):
                if pixel:
                    return len(row) - (1 + index)
            return None

        def makePixelProfile(pixels, func):
            result = []
            for row in pixels:
                result.append(func(row))
            return result

        profile0 = makePixelProfile(pixels0, rightRowProfile)
        profile1 = makePixelProfile(pixels1, leftRowProfile)

#        def makeRowProfile(row, func):
#            result = None
#            for index, pixel in enumerate(row):
#                if pixel:
#                    if result is not None:
#                        result = func(result, index)
#                    else:
#                        result = index
#            return result
#
#        def makePixelProfile(pixels, func):
#            result = []
#            for row in pixels:
#                result.append(makeRowProfile(row, func))
#            return result
#
#        profile0 = makePixelProfile(pixels0, max)
#        profile1 = makePixelProfile(pixels1, min)
#        print 'profile0', profile0
#        print 'profile1', profile1
        contactAdvance = None
        for edge0, edge1 in zip(profile0, profile1):
            if edge0 is None or edge1 is None:
                continue
            diff = 1 + edge0 - edge1
#            print 'diff', diff
#            print 'edge0, edge1', edge0, edge1, 'diff', diff
            if contactAdvance is None:
                contactAdvance = diff
            else:
                contactAdvance = max(contactAdvance, diff)

#        print 'contactAdvance', contactAdvance

        if contactAdvance is None or intrusionTolerancePixels == 0:
            return contactAdvance

        def getProfileOverlap(advance):
#            print
#            print 'getProfileOverlap'
            intrusionTotal = 0
            extrusionTotal = 0
            nonIntrusionCount = 0
            for edge0, edge1 in zip(profile0, profile1):
                if edge0 is None or edge1 is None:
                    continue
                diff = 1 + edge0 - edge1
                rowIntrusion = max(0, diff - advance)
                rowExtrusion = max(0, advance - diff)
#                print 'edge0, edge1', edge0, edge1, 'diff', diff, 'advance', advance, 'rowIntrusion', rowIntrusion, 'rowExtrusion', rowExtrusion
                intrusionTotal += rowIntrusion
                extrusionTotal += rowExtrusion
                if rowIntrusion <= 0:
                    nonIntrusionCount += 1
            return intrusionTotal, extrusionTotal, nonIntrusionCount


#        width0 = len(pixels0[0])
#        width1 = len(pixels1[0])
#        print 'contactAdvance', contactAdvance
#        print 'tolerancePixels', tolerancePixels
        offsetAdvance = contactAdvance
#        for offset in xrange(1, min(width0, width1)):
        for offset in xrange(1, contactAdvance + 1):
            advance = contactAdvance - offset
            intrusionTotal, extrusionTotal, nonIntrusionCount = getProfileOverlap(advance)
#            print 'intrusionTotal, extrusionTotal, nonIntrusionCount', intrusionTotal, extrusionTotal, nonIntrusionCount, 'intrusionTolerancePixels', intrusionTolerancePixels, 'minNonIntrusionCount', minNonIntrusionCount
            if intrusionTotal > extrusionTotal:
                return offsetAdvance
            if intrusionTotal > intrusionTolerancePixels:
                return offsetAdvance
            minNonIntrusionCount
            if nonIntrusionCount < minNonIntrusionCount:
                return offsetAdvance

#            overlapPixels = getProfileOverlap(advance)
##            print 'overlapPixels', overlapPixels
#            if overlapPixels > tolerancePixels:
#                return offsetAdvance

#            return offsetAdvance

            offsetAdvance = advance

        return offsetAdvance


    def findDisparities(self):

        disparities = []
        glyphs = self.dstUfoFont.getGlyphs()
#        total = len(glyphs) * len(glyphs)
#        count = 0
#        startTime = time.time()
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))
        for ufoglyph0 in glyphs:
            for ufoglyph1 in glyphs:
                key = (ufoglyph0.unicode,
                       ufoglyph1.unicode,)
                if key not in self.advanceMap:
                    continue

                disparity = TFSMap()
                disparity.dstUfoGlyph0 = ufoglyph0
                disparity.dstUfoGlyph1 = ufoglyph1

#                disparity.srcXAdvance = disparity.srcUfoGlyph0.xAdvance
                disparity.dstAdvance = int(round(self.advanceMap[key]))
                disparity.dstXAdvance = disparity.dstUfoGlyph0.xAdvance
                disparity.dstKerning = disparity.dstAdvance - disparity.dstXAdvance


                disparity.srcUfoGlyph0 = self.srcUfoFont.getGlyphByName(ufoglyph0.name)
                if disparity.srcUfoGlyph0 is None:
                    raise Exception('Could not find glyph by name: %s %s' % (str(ufoglyph0.name),
                                                                             str(ufoglyph0.unicode)))
                disparity.srcUfoGlyph1 = self.srcUfoFont.getGlyphByName(ufoglyph1.name)
                if disparity.srcUfoGlyph1 is None:
                    raise Exception('Could not find glyph by name: %s %s' % (str(ufoglyph1.name),
                                                                             str(ufoglyph1.unicode)))

                disparity.srcKerning = self.srcUfoFont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
                if disparity.srcKerning is None:
                    disparity.srcKerning = 0
                disparity.srcXAdvance = disparity.srcUfoGlyph0.xAdvance
                disparity.srcAdvance = disparity.srcUfoGlyph0.xAdvance + disparity.srcKerning


                disparity.srcContours0 = self.getSrcGlyphContours(disparity.srcUfoGlyph0)
                disparity.srcContours1 = self.getSrcGlyphContours(disparity.srcUfoGlyph1)

                disparity.srcMinmax0 = self.getSrcCachedValue('getCachedMinmax %s' % ufoglyph0.name, getCachedMinmax, disparity.srcContours0)
                disparity.srcMinmax1 = self.getSrcCachedValue('getCachedMinmax %s' % ufoglyph1.name, getCachedMinmax, disparity.srcContours1)
                disparity.srcOffset = disparity.srcAdvance + (-disparity.srcMinmax0.maxX) + (disparity.srcMinmax1.minX)

                disparity.dstContours0 = self.getGlyphContours(ufoglyph0)
                disparity.dstContours1 = self.getGlyphContours(ufoglyph1)
                disparity.dstMinmax0 = self.getDstCachedValue('getCachedMinmax %s' % ufoglyph0.name, getCachedMinmax, disparity.dstContours0)
                disparity.dstMinmax1 = self.getDstCachedValue('getCachedMinmax %s' % ufoglyph1.name, getCachedMinmax, disparity.dstContours1)
                disparity.dstOffset = disparity.dstAdvance + (-disparity.dstMinmax0.maxX) + (disparity.dstMinmax1.minX)

                disparity.offsetDifference = abs(disparity.srcOffset - disparity.dstOffset)
                disparity.advanceDifference = abs(disparity.dstAdvance - disparity.srcAdvance)

                if disparity.offsetDifference != 0:
                    disparities.append(disparity)

        def compareDisparities(disparity0, disparity1):
            return cmp(disparity0.offsetDifference, disparity1.offsetDifference)

        disparities.sort(compareDisparities, reverse=True)
        return disparities


    def logDisparities(self):

        renderLog = self.log_dst is not None
        if not renderLog:
            return

        disparities = self.findDisparities()

        '''
        We're only interested in the top 100 disparities.
        '''
        disparities = disparities[:100]

        def getDisparityFilename(index):
            return 'disparity-%d.html' % index

        disparityLinkMaps = []
        for index, disparity in enumerate(disparities):
            disparityLinkMaps.append({ 'filename': getDisparityFilename(index),
                                      'name': str(index + 1),
                                      })

        for index, disparity in enumerate(disparities):

            filenamePrefix = 'disparity-%d' % index
            phase = 0
            oldAdvanceSvg = self.renderSvgScene(filenamePrefix + '-old-advance',
                                             pathTuples = (
                                                           ( 0x7f7faf7f, disparity.srcContours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(disparity.srcAdvance, 0)) for contour in disparity.srcContours1], ),
                                                           ),
                                             hGuidelines = ( disparity.srcAdvance, ) )
            phase += 1

            newAdvanceSvg = self.renderSvgScene(filenamePrefix + '-new-advance',
                                             pathTuples = (
                                                           ( 0x7f7faf7f, disparity.dstContours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(disparity.dstAdvance, 0)) for contour in disparity.dstContours1], ),
                                                           ),
                                             hGuidelines = ( disparity.dstAdvance, ) )
            phase += 1

            import tfs.common.TFSProject as TFSProject
            mustache_template_file = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'autokern_disparity_template.txt'))
            with open(mustache_template_file, 'rt') as f:
                mustache_template = f.read()

            pageTitle = u'pyautokern Log: Disparity %s vs. %s' % ( formatGlyphName(disparity.dstUfoGlyph0),
                                                                   formatGlyphName(disparity.dstUfoGlyph1), )

            def formatEmScalar(value):
                return '%0.3f em' % (value / float(self.units_per_em))

            def formatGlyphMap(glyph, srcMinmax, dstMinmax):
                return {
                           'glyphName': formatGlyphName(glyph),
                           'srcMinX': formatEmScalar(srcMinmax.minX),
                           'srcMaxX': formatEmScalar(srcMinmax.maxX),
                           'dstMinX': formatEmScalar(dstMinmax.minX),
                           'dstMaxX': formatEmScalar(dstMinmax.maxX),
                        }

            mustacheMap = {
                           'kerningLogFilename': self.getKerningPairHtmlFilename(disparity.dstUfoGlyph0,
                                                                                 disparity.dstUfoGlyph1),
                           'pageTitle': pageTitle,
                           'minmax0': disparity.dstMinmax0,
                           'minmax1': disparity.dstMinmax1,
                           'dstAdvance': formatEmScalar(disparity.dstAdvance),
                           'srcAdvance': formatEmScalar(disparity.srcAdvance),
                           'advanceDifference': formatEmScalar(disparity.advanceDifference),
                           'srcOffset': formatEmScalar(disparity.srcOffset),
                           'dstOffset': formatEmScalar(disparity.dstOffset),
                           'offsetDifference': formatEmScalar(disparity.offsetDifference),
                           'srcKerning': formatEmScalar(disparity.srcKerning),
                           'srcXAdvance': formatEmScalar(disparity.srcXAdvance),
                           'dstXAdvance': formatEmScalar(disparity.dstXAdvance),
                           'dstKerning': formatEmScalar(disparity.dstKerning),

                           'min_distance': formatEmScalar(self.min_distance),
                           'max_distance': formatEmScalar(self.max_distance),

                           'oldAdvanceSvg': oldAdvanceSvg,
                           'newAdvanceSvg': newAdvanceSvg,

                           'glyph0': formatGlyphName(disparity.dstUfoGlyph0),
                           'glyph1': formatGlyphName(disparity.dstUfoGlyph1),

                           'glyphMaps': ( formatGlyphMap(disparity.dstUfoGlyph0, disparity.srcMinmax0, disparity.dstMinmax0),
                                          formatGlyphMap(disparity.dstUfoGlyph1, disparity.srcMinmax1, disparity.dstMinmax1),
                                          ),
                           'disparityLinkMaps': disparityLinkMaps,
                           'firstDisparityLink': getDisparityFilename(0),
                           'lastDisparityLink': getDisparityFilename(len(disparities) - 1),
                           }
            if index > 0:
                mustacheMap['prevDisparityLink'] = {'filename': getDisparityFilename(index - 1), }
            if index + 1 < len(disparities):
                mustacheMap['nextDisparityLink'] = {'filename': getDisparityFilename(index + 1), }

            for key in ( 'ascender',
                         'descender',
                        ):
                mustacheMap[key] = formatEmScalar(getattr(self.dstUfoFont.info, key))

            for key in (
                         'unitsPerEm',
                         'familyName',
                         'styleName',
                         'fullName',
                         'fontName',
                        ):
                mustacheMap[key] = getattr(self.dstUfoFont.info, key)

            import pystache
            logHtml = pystache.render(mustache_template, mustacheMap)

            logFilename = getDisparityFilename(index)
            logFile = os.path.abspath(os.path.join(self.html_folder, logFilename))
            with open(logFile, 'wt') as f:
                # TODO: explicitly encode unicode
                f.write(logHtml)

#    def convertToPixelUnits(self, value):
#        RASTERIZE_CELL_SIZE = self.precision
#        return int(math.ceil(value / float(RASTERIZE_CELL_SIZE)))

    def getDstCachedValue(self, key, func, *argv):
        if key in self.dstValueCache:
            return self.dstValueCache[key]
        result = func(*argv)
        self.dstValueCache[key] = result
        return result

    def getSrcCachedValue(self, key, func, *argv):
        if key in self.srcValueCache:
            return self.srcValueCache[key]
        result = func(*argv)
        self.srcValueCache[key] = result
        return result


    def getFilenamePrefixPair(self, prefix, ufoglyph0, ufoglyph1):
        return '%s-%s-%s' % ( prefix,
                              formatUnicode(ufoglyph0.unicode),
                              formatUnicode(ufoglyph1.unicode), )

    def getKerningPairFilenamePrefix(self, ufoglyph0, ufoglyph1):
        return self.getFilenamePrefixPair('autokern', ufoglyph0, ufoglyph1)

    def getKerningPairHtmlFilename(self, ufoglyph0, ufoglyph1):
        return self.getKerningPairFilenamePrefix(ufoglyph0, ufoglyph1) + '.haml'

    def processKerningPair(self, ufoglyph0, ufoglyph1):
        '''
        TODO: handle empty glyphs with no contours
        '''

        self.timing.mark('processKerningPair.0.')

        if self.isCombiningGlyph(ufoglyph0) or self.isCombiningGlyph(ufoglyph1):
            return

#        print 'processKerningPair'

        debugKerning = True
        debugKerning = False

        renderLog = self.log_dst is not None

        RASTERIZE_CELL_SIZE = self.precision

        contours0 = self.getGlyphContours(ufoglyph0)
        contours1 = self.getGlyphContours(ufoglyph1)
        if (not contours0) or (not contours1):
            return

        self.timing.mark('processKerningPair.01')

#            return self.inflatePixelBlock(pixels1, min_distance, RASTERIZE_CELL_SIZE)
        minmax0 = self.getDstCachedValue('getCachedMinmax %s' % ufoglyph0.name, getCachedMinmax, contours0)
        minmax1 = self.getDstCachedValue('getCachedMinmax %s' % ufoglyph1.name, getCachedMinmax, contours1)

#        minmax0 = minmaxPaths(contours0)
#        minmax1 = minmaxPaths(contours1)

        self.timing.mark('processKerningPair.02')

        pixels0 = self.getGlyphPixels(ufoglyph0)
        pixels1 = self.getGlyphPixels(ufoglyph1)

        self.timing.mark('processKerningPair.03')

#        pixels0 = self.rasterizeGlyph(ufoglyph0, RASTERIZE_CELL_SIZE)
#        pixels1 = self.rasterizeGlyph(ufoglyph1, RASTERIZE_CELL_SIZE)

        if (pixels0 is None) or (pixels1 is None):
            return

        if debugKerning:
            self.dumpPixelBlock('pixels0', pixels0)
            self.dumpPixelBlock('pixels1', pixels1)

        def convertToPixelUnits(value):
            return int(math.ceil(value / float(RASTERIZE_CELL_SIZE)))

        min_distance = self.min_distance_ems * self.dstUfoFont.units_per_em
        if debugKerning:
            print 'min_distance', min_distance
#        min_distance_pixels = self.convertToPixelUnits(min_distance, RASTERIZE_CELL_SIZE)
#        if debugKerning:
#            print 'min_distance_pixels', min_distance_pixels

        max_distance = self.max_distance_ems * self.dstUfoFont.units_per_em
        if debugKerning:
            print 'max_distance', max_distance
#        max_distance_pixels = self.convertToPixelUnits(max_distance, RASTERIZE_CELL_SIZE)
#        if debugKerning:
#            print 'max_distance_pixels', max_distance_pixels

#        pixels0 = self.padPixels(pixels0, self.convertToPixelUnits(max_distance, RASTERIZE_CELL_SIZE))
#        pixels1 = self.padPixels(pixels1, self.convertToPixelUnits(max_distance, RASTERIZE_CELL_SIZE))
#
#        self.timing.mark('processKerningPair.04')
#
#        if debugKerning:
#            self.dumpPixelBlock('pixels0', pixels0)
#            self.dumpPixelBlock('pixels1', pixels1)

        def getPixelsPlusMinDistance():
            return self.inflatePixelBlock(pixels1, min_distance, RASTERIZE_CELL_SIZE)
        pixels1_plusMin = self.getDstCachedValue('pixels1_plusMin %s' % ufoglyph1.name, getPixelsPlusMinDistance)

#        pixels1_plusMin = self.inflatePixelBlock(pixels1, min_distance, RASTERIZE_CELL_SIZE)
        self.timing.mark('processKerningPair.1')
        if debugKerning:
            self.dumpPixelBlock('pixels1_plusMin', pixels1_plusMin)

#        print 'pixels0', len(pixels0), 'pixels1', len(pixels1), 'pixels1_plusMin', len(pixels1_plusMin)

        minAdvancePixels = self.findMinAdvance(pixels0, pixels1_plusMin)
        self.timing.mark('processKerningPair.2')
        if minAdvancePixels is None:
            '''
            If no collision between glyphs (ie. underline and hyphen),
            default to conservative spacing.
            '''
            minAdvance = minmax0.maxX + min_distance - minmax1.minX
        else:
            minAdvance = RASTERIZE_CELL_SIZE * minAdvancePixels
        if debugKerning:
            print 'minAdvance', minAdvance, 'minAdvancePixels', minAdvancePixels

#        self.minAdvanceMap[(ufoglyph0.unicode,
#                            ufoglyph1.unicode,)] = minAdvance

        height0 = minmax0.maxY - minmax0.minY
        height1 = minmax1.maxY - minmax1.minY
        maxGlyphHeight = max(height0, height1)

        def getPixelsPlusMaxDistance():
            return self.inflatePixelBlock(pixels1, max_distance, RASTERIZE_CELL_SIZE)
        pixels1_plusMax = self.getDstCachedValue('pixels1_plusMax %s' % ufoglyph1.name, getPixelsPlusMaxDistance)

#        print 'pixels0', len(pixels0), 'pixels1', len(pixels1), 'pixels1_plusMin', len(pixels1_plusMin), 'pixels1_plusMax', len(pixels1_plusMax)


#        pixels1_plusMax = self.inflatePixelBlock(pixels1, max_distance, RASTERIZE_CELL_SIZE)
        if debugKerning:
            self.dumpPixelBlock('pixels1_plusMax', pixels1_plusMax)

        self.timing.mark('processKerningPair.3')

        intrusion_tolerance = self.intrusion_tolerance * max_distance * maxGlyphHeight
        intrusion_tolerance_pixels = int(round(float(intrusion_tolerance) / (RASTERIZE_CELL_SIZE * RASTERIZE_CELL_SIZE)))

        min_non_intrusion = self.min_non_intrusion_ems * self.dstUfoFont.units_per_em
        min_non_intrusion_pixels = int(round(float(min_non_intrusion) / RASTERIZE_CELL_SIZE))
        if debugKerning:
            print 'min_non_intrusion', min_non_intrusion, 'min_non_intrusion_pixels', min_non_intrusion_pixels

        maxAdvance = minmax0.maxX + max_distance - minmax1.minX
        if debugKerning:
            print 'maxAdvance', maxAdvance

        intrudingAdvancePixels = self.findMinAdvance(pixels0, pixels1_plusMax,
                                               intrusionTolerancePixels=intrusion_tolerance_pixels,
                                               minNonIntrusionCount=min_non_intrusion_pixels)
        self.timing.mark('processKerningPair.4')
        if intrudingAdvancePixels is None:
            '''
            No collision between glyphs (ie. underline and hyphen).
            Default to conservative spacing.
            '''
            intrudingAdvance = maxAdvance
        else:
            intrudingAdvance = RASTERIZE_CELL_SIZE * intrudingAdvancePixels
        if debugKerning:
            print 'intrudingAdvance', intrudingAdvance, 'intrudingAdvancePixels', intrudingAdvancePixels

        '''
        Now combine results into the final advance value.
        1. Start with the "intruding advance."
        2. Make sure advance is at least the "minimum advance."
        3. Make sure advance is no greater than the "glyph width intrusion limit".
        '''
        advance = max(minAdvance, intrudingAdvance)

        width0 = minmax0.maxX - minmax0.minX
        width1 = minmax1.maxX - minmax1.minX
        intrusion_limit_width = self.intrusion_limit_glyph_width_fraction * min(width0, width1)
        advanceLimit = (minmax0.maxX - minmax1.minX) - intrusion_limit_width
#        print 'intrusion_limit', intrusion_limit_width, 'advance', advance, 'advanceLimit', advanceLimit
        advance = max(advance, advanceLimit)
#        print 'advanceLimit', advanceLimit, 'advance', advance


        self.advanceMap[(ufoglyph0.unicode,
                         ufoglyph1.unicode,)] = advance

        if debugKerning:
            print '\t', ufoglyph0.unicode, ufoglyph1.unicode, advance
#        import sys
#        sys.exit(0)

        self.timing.mark('processKerningPair.5')

        if renderLog:
#            from tfs.common.TFSSvg import *
            filenamePrefix = self.getKerningPairFilenamePrefix(ufoglyph0, ufoglyph1)
            phase = 1

            srcufoglyph0 = self.srcUfoFont.getGlyphByName(ufoglyph0.name)
            if srcufoglyph0 is None:
                raise Exception('Could not find glyph by name: %s %s' % (str(ufoglyph0.name),
                                                                         str(ufoglyph0.unicode)))
            srcufoglyph1 = self.srcUfoFont.getGlyphByName(ufoglyph1.name)
            if srcufoglyph1 is None:
                raise Exception('Could not find glyph by name: %s %s' % (str(ufoglyph1.name),
                                                                         str(ufoglyph1.unicode)))

            srcContours0 = self.getSrcGlyphContours(srcufoglyph0)
            srcContours1 = self.getSrcGlyphContours(srcufoglyph1)
            srcKerning = self.dstUfoFont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
            if srcKerning is None:
                srcKerning = 0
            srcAdvance = srcufoglyph0.xAdvance + srcKerning

            srcminmax0 = self.getSrcCachedValue('getCachedMinmax %s' % ufoglyph0.name, getCachedMinmax, srcContours0)
            srcminmax1 = self.getSrcCachedValue('getCachedMinmax %s' % ufoglyph1.name, getCachedMinmax, srcContours1)

            srcAdvanceAdjusted = srcAdvance + (-srcminmax0.minX) + srcminmax1.minX
            advanceAdjusted = advance + (-minmax0.minX) + minmax1.minX

            srcSpacingSvg = self.renderSvgScene(None,
#                                                filenamePrefix + '-src-spacing',
                                             pathTuples = (
                                                           ( 0x7f7faf7f, srcContours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(srcAdvance, 0)) for contour in srcContours1], ),
                                                           ),
                                             hGuidelines = ( srcAdvance, ) )
            phase += 1

            self.timing.mark('processKerningPair.6')

            naiveAdvancePixels = self.findMinAdvance(pixels0, pixels1)
            if naiveAdvancePixels is None:
                '''
                No collision between glyphs (ie. underline and hyphen).
                Default to conservative spacing.
                '''
                naiveAdvance = minmax0.maxX - minmax1.minX
            else:
                naiveAdvance = RASTERIZE_CELL_SIZE * naiveAdvancePixels
            if debugKerning:
                print 'naiveAdvancePixels', naiveAdvancePixels, 'naiveAdvance', naiveAdvance

#            intrudingAdvanceRawPixels = self.findMinAdvance(pixels0, pixels1_plusMax)
#            intrudingAdvanceRaw = RASTERIZE_CELL_SIZE * intrudingAdvanceRawPixels
#            print 'intrudingAdvanceRaw', intrudingAdvanceRaw, 'intrudingAdvanceRawPixels', intrudingAdvanceRawPixels

            self.timing.mark('processKerningPair.6a')

            naiveSpacingSvg = self.renderSvgScene(None,
#                                                  filenamePrefix + '-naive-spacing',
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(naiveAdvance, 0)) for contour in contours1], ),
                                                           ),
                                             hGuidelines = ( naiveAdvance, ) )
            phase += 1

            minDistanceSpacingSvg = self.renderSvgScene(None,
#                                                        filenamePrefix + '-min-spacing',
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(minAdvance, 0)) for contour in contours1], ),
                                                           ),
                                             hGuidelines = ( minAdvance, ) )
            phase += 1

            maxDistanceSpacingSvg = self.renderSvgScene(None,
#                                                        filenamePrefix + '-max-spacing',
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(maxAdvance, 0)) for contour in contours1], ),
                                                           ),
                                             hGuidelines = ( maxAdvance, ) )
            phase += 1
            intrudingAdvanceSpacingSvg = self.renderSvgScene(None,
#                                                             filenamePrefix + '-intruding-advance',
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(intrudingAdvance, 0)) for contour in contours1], ),
                                                           ),
                                             hGuidelines = ( intrudingAdvance, ) )
            phase += 1
            finalAdvanceSpacingSvg = self.renderSvgScene(None,
#                                                         filenamePrefix + '-advance',
                                             pathTuples = (
                                                           ( 0x7f7faf7f, contours0, ),
                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(advance, 0)) for contour in contours1], ),
                                                           ),
                                             hGuidelines = ( advance, ) )
            phase += 1
#            finalKerningSvg = self.renderSvgScene(
#                                             filenamePrefix, phase, 'ignore',
#                                             pathTuples = (
#                                                           ( 0x7f7faf7f, contours0, ),
#                                                           ( 0x7f7f7faf, [contour.applyPlus(TFSPoint(advance - ufoglyph0.xAdvance, 0)) for contour in contours1], ),
#                                                           ),
#                                             hGuidelines = ( advance - ufoglyph0.xAdvance, ) )
#            phase += 1
            self.timing.mark('processKerningPair.8')

            import tfs.common.TFSProject as TFSProject
            mustache_template_file = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'autokern_pair_pixel_template.txt'))
            with open(mustache_template_file, 'rt') as f:
                mustache_template = f.read()

            pageTitle = u'pyautokern Log: %s vs. %s' % ( formatGlyphName(ufoglyph0),
                                                         formatGlyphName(ufoglyph1), )

            def formatEmScalar(value):
                return '%0.3f em' % (value / float(self.units_per_em))

            def formatGlyphMap(glyph, glyphMinmax):
                return {
                           'glyphName': formatGlyphName(glyph),
                           'minX': formatEmScalar(glyphMinmax.minX),
                           'maxX': formatEmScalar(glyphMinmax.maxX),
                           'minY': formatEmScalar(glyphMinmax.minY),
                           'maxY': formatEmScalar(glyphMinmax.maxY),
                        }

            mustacheMap = {
                           'pageTitle': pageTitle,
                           'minmax0': minmax0,
                           'minmax1': minmax1,
#                           'naiveSpacing': formatEmScalar(naiveSpacing),
#                           'minDistanceSpacing': formatEmScalar(minDistanceSpacing),
#                           'roundingSpacing': formatEmScalar(roundingSpacing),
                           'naiveAdvance': formatEmScalar(naiveAdvance),
                           'minAdvance': formatEmScalar(minAdvance),
                           'maxAdvance': formatEmScalar(maxAdvance),
                           'intrudingAdvance': formatEmScalar(intrudingAdvance),
                           'advance': formatEmScalar(advance),
                           'srcAdvance': formatEmScalar(srcAdvance),
                           'srcAdvanceAdjusted': formatEmScalar(srcAdvanceAdjusted),
                           'advanceAdjusted': formatEmScalar(advanceAdjusted),

#                           'maxAdvance': formatEmScalar(maxAdvance),
                           'min_distance': formatEmScalar(self.min_distance),
                           'max_distance': formatEmScalar(self.max_distance),
#                           'intrusion_tolerance': formatEmScalar(self.intrusion_tolerance),
                           'min_non_intrusion': formatEmScalar(min_non_intrusion),
#                           'rounding': formatEmScalar(self.rounding),

                           'srcSpacingSvg': srcSpacingSvg,
                           'naiveSpacingSvg': naiveSpacingSvg,
                           'minDistanceSpacingSvg': minDistanceSpacingSvg,
                           'maxDistanceSpacingSvg': maxDistanceSpacingSvg,
                           'intrudingAdvanceSpacingSvg': intrudingAdvanceSpacingSvg,
                           'finalAdvanceSpacingSvg': finalAdvanceSpacingSvg,
#                           'roundingSpacingSvg': roundingSpacingSvg,

                           'glyph0': formatGlyphName(ufoglyph0),
                           'glyph1': formatGlyphName(ufoglyph1),

                           'glyphMaps': ( formatGlyphMap(ufoglyph0, minmax0),
                                          formatGlyphMap(ufoglyph1, minmax1),
                                          )
                           }

            for key in ( 'ascender',
                         'descender',
                        ):
                mustacheMap[key] = formatEmScalar(getattr(self.dstUfoFont.info, key))

            for key in (
                         'unitsPerEm',
                         'familyName',
                         'styleName',
                         'fullName',
                         'fontName',
                        ):
                mustacheMap[key] = getattr(self.dstUfoFont.info, key)

            import pystache
            logHtml = pystache.render(mustache_template, mustacheMap)

            logFilename = self.getKerningPairHtmlFilename(ufoglyph0, ufoglyph1)
            logFile = os.path.abspath(os.path.join(self.html_folder, logFilename))
            with open(logFile, 'wt') as f:
                # TODO: explicitly encode unicode
                f.write(logHtml)

#            import sys
#            sys.exit(0)

        self.timing.mark('processKerningPair.9')


    def processAllKerningPairs(self):

#        self.advanceMap = {(67, 79): 675, (65, 67): 575, (84, 67): 1025, (88, 69): 1063.0, (66, 65): 350, (67, 85): 675, (68, 76): 675, (69, 90): 680.0, (66, 76): 975, (69, 87): 875, (65, 84): 225, (71, 84): 300, (76, 66): 675, (85, 84): 675, (89, 67): 875, (65, 89): 300, (84, 85): 800, (85, 65): 375, (90, 73): 875, (90, 67): 875, (87, 66): 1375, (76, 88): -50, (66, 87): 975, (79, 84): 1025, (87, 79): 1375, (66, 66): 975, (73, 88): -150, (68, 65): 400, (85, 69): 875, (70, 68): 525, (85, 90): 400, (89, 79): 875, (65, 87): 575, (79, 67): 1375, (76, 71): 250, (85, 87): 1025, (84, 87): 1025, (65, 68): 575, (84, 66): 1025, (87, 84): 1025, (85, 68): 1025, (67, 73): 675, (65, 73): 575, (87, 65): 725, (84, 69): 950, (66, 88): 250, (67, 90): 250, (79, 65): 725, (73, 70): 250, (69, 67): 875, (66, 71): 650, (79, 88): 550, (68, 70): 675, (70, 65): 300, (79, 85): 1150, (90, 65): 700, (79, 79): 1375, (70, 84): 300, (79, 70): 950, (76, 68): 675, (89, 84): 525, (65, 71): 550, (76, 87): 675, (85, 71): 650, (67, 68): 675, (89, 73): 875, (73, 76): 675, (87, 68): 1375, (69, 73): 875, (67, 89): 250, (73, 65): 25, (69, 70): 880.0, (88, 73): 1375, (71, 71): 525, (70, 66): 525, (79, 69): 950, (76, 73): 675, (90, 84): 525, (89, 87): 875, (65, 66): 575, (76, 84): 325, (67, 67): 675, (89, 68): 875, (73, 79): 675, (79, 87): 1375, (69, 76): 875, (79, 89): 750, (67, 84): 350, (88, 67): 1375, (69, 89): 680.0, (90, 89): 675, (88, 87): 1375, (68, 88): 75, (70, 79): 525, (71, 87): 525, (76, 67): 675, (79, 76): 1375, (65, 88): -250, (84, 90): 600, (84, 65): 525, (84, 89): 600, (76, 89): 50, (66, 84): 625, (89, 71): 875, (90, 88): 250, (69, 79): 875, (66, 67): 975, (68, 66): 675, (84, 79): 1025, (70, 69): 530.0, (71, 73): 525, (85, 89): 400, (71, 90): 325, (84, 88): 200, (89, 88): 250, (87, 87): 1375, (85, 67): 1025, (90, 69): 880.0, (84, 70): 800, (66, 89): 350, (89, 66): 875, (73, 69): 250, (69, 66): 875, (66, 68): 975, (88, 66): 1375, (73, 90): 50, (71, 67): 525, (68, 71): 675, (89, 69): 880.0, (70, 70): 525, (71, 76): 525, (70, 85): 525, (71, 89): 325, (76, 69): 250, (85, 73): 1025, (65, 70): 350, (70, 88): -75, (87, 90): 750, (85, 70): 600, (67, 71): 525, (90, 70): 850, (87, 71): 950, (66, 90): 350, (67, 88): 75, (68, 73): 675, (69, 69): 875, (66, 73): 975, (90, 85): 850, (73, 85): 450, (71, 70): 525, (68, 68): 675, (70, 67): 525, (90, 87): 875, (68, 87): 675, (79, 68): 1375, (85, 76): 1025, (88, 84): 1150, (65, 65): 575, (87, 89): 750, (76, 85): 450, (67, 66): 675, (84, 84): 675, (67, 87): 675, (73, 67): 675, (69, 88): 150, (88, 90): 1050, (88, 65): 950, (71, 69): 780.0, (68, 89): 400, (69, 85): 650, (70, 76): 525, (88, 68): 1375, (68, 84): 350, (90, 66): 875, (90, 76): 875, (76, 79): 675, (85, 79): 1025, (67, 76): 675, (79, 66): 1375, (65, 76): 575, (76, 90): 50, (66, 85): 825, (67, 65): 275, (89, 70): 850, (73, 73): 675, (87, 73): 1375, (68, 67): 675, (66, 79): 975, (88, 85): 1350, (85, 88): 200, (65, 85): 350, (70, 73): 525, (71, 85): 525, (76, 65): 25, (85, 85): 800, (65, 90): 300, (76, 76): 675, (85, 66): 1025, (89, 76): 875, (65, 79): 575, (87, 67): 1375, (84, 71): 875, (89, 65): 700, (73, 68): 675, (87, 76): 1375, (69, 65): 225, (66, 69): 600, (73, 89): 50, (71, 66): 525, (88, 89): 1050, (70, 71): 525, (71, 79): 525, (90, 90): 675, (71, 88): -75, (76, 70): 250, (89, 90): 675, (65, 69): 800, (70, 89): 325, (87, 85): 1150, (84, 73): 1025, (79, 90): 750, (67, 70): 525, (88, 70): 1300, (90, 71): 875, (87, 70): 950, (84, 68): 1025, (73, 71): 250, (90, 79): 875, (69, 68): 875, (66, 70): 650, (73, 84): 325, (71, 65): 300, (68, 69): 500, (88, 76): 1375, (88, 79): 1375, (89, 89): 675, (88, 71): 1300, (84, 76): 1025, (70, 87): 525, (79, 71): 950, (89, 85): 850, (70, 90): 325, (87, 88): 550, (67, 69): 375, (87, 69): 950, (73, 66): 675, (68, 79): 675, (69, 71): 880.0, (73, 87): 675, (71, 68): 525, (68, 90): 400, (69, 84): 875, (88, 88): 775, (79, 73): 1375, (68, 85): 675, (90, 68): 875}
#        return

#        count = 0

        glyphs = self.dstUfoFont.getGlyphs()
        total = len(glyphs) * len(glyphs)
        count = 0
        startTime = time.time()
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))
        for ufoglyph0 in glyphs:
            for ufoglyph1 in glyphs:
                glyphNamesToKern = ('grave',
                                    'acute',
                                    'AE',
                                    'backslash',
                                    'numbersign',
                                    'aacute',
                                    'slash',
                                    'd',
                                    '4',
                                    'h',
                                    'H',
                                    'A',
                                    'T',
                                    'V',
                                    'L',
                                    'J',
                                    'Y',
                                    'W',
                                    'N',
                                    'B',
                                    )
                if not ((ufoglyph0.name in glyphNamesToKern) and (ufoglyph1.name in glyphNamesToKern)):
                    count += 1
                    continue


#                maxUnicode = 0x25
#                maxUnicode = 0x22
#                maxUnicode = 0x30
#                maxUnicode = 0x40
#                if not (ufoglyph0.unicode <= maxUnicode and ufoglyph1.unicode <= maxUnicode):
#                    continue

#                if ufoglyph0.unicode != 0x41 or ufoglyph1.unicode != 0x42:
#                    continue
#                if ufoglyph0.unicode != 0x41:
#                    continue

#        for ufoglyph0 in self.dstUfoFont.getGlyphs():
#            for ufoglyph1 in self.dstUfoFont.getGlyphs():
                self.processKerningPair(ufoglyph0, ufoglyph1)

                count += 1
                remaining = ''
                if count % 10 == 0:
                    elapsedTime = time.time() - startTime
#                    print 'elapsedTime', elapsedTime, 'total', total
                    averageTime = elapsedTime / float(count)
#                    print 'averageTime', averageTime
                    totalTime = averageTime * total
                    remainingTime = totalTime - elapsedTime
                    remaining = '%0.0f seconds remaining, %0.2f seconds average' % (remainingTime, averageTime,)

                def formatUnicode(value):
                    if value is None:
                        return 'None'
                    else:
                        return '0x%X' % ( value, )
#                print 'ufoglyph0', ufoglyph0.unicode, ufoglyph0.name, 'ufoglyph1', ufoglyph1.unicode, ufoglyph1.name
                if count % 10 == 0:
                    print '\t', '%s %s vs. %s %s (%0.2f%%)' % ( ufoglyph0.name,
                                                          formatUnicode(ufoglyph0.unicode),
                                                          ufoglyph1.name,
                                                          formatUnicode(ufoglyph1.unicode),
                                                          100 * count / float(total),), '\t', remaining

#                count += 1
#                if count > 3:
#                    return

#        sys.exit(0)
        print 'self.advanceMap =', repr(self.advanceMap)
        print


    def configure(self):

        ufo_src = self.ufo_src
        if ufo_src is None:
            raise Exception('Missing ufo_src')
        if not (os.path.exists(ufo_src) and os.path.isdir(ufo_src) and os.path.basename(ufo_src).lower().endswith('.ufo')):
            raise Exception('Invalid ufo_src: %s' % ufo_src)

    #    testFont = os.path.abspath(os.path.join('..', '..', 'data', 'TFSTest Plain.ufo'))
#        self.dstUfoFont = TFSFontFromFile(ufo_src)
        self.srcUfoFont = TFSFontFromFile(ufo_src)
        self.dstUfoFont = TFSFontFromFile(ufo_src)
#        self.dstUfoFont = TFSFontFromFile(ufo_src)


        if self.ufo_dst is None:
            raise Exception('Missing ufo_dst')
        if os.path.exists(self.ufo_dst):
            if os.path.isdir(self.ufo_dst):
                shutil.rmtree(self.ufo_dst)
            elif os.path.isfile(self.ufo_dst):
                os.unlink(self.ufo_dst)
            if os.path.exists(self.ufo_dst):
                raise Exception('Could not overwrite: %s' % (self.ufo_dst,))


        log_dst = self.log_dst
        if log_dst is None:
            self.log_dst = None
    #        raise Exception('Missing log_dst')
            pass
        else:
            OVERWRITE_LOGS = True
#            OVERWRITE_LOGS = False

            if OVERWRITE_LOGS:
                if os.path.exists(log_dst):
                    shutil.rmtree(log_dst)
                if os.path.exists(log_dst):
                    raise Exception('Could not clear log_dst: %s' % log_dst)

            if not os.path.exists(log_dst):
                os.mkdir(log_dst)
            if not (os.path.exists(log_dst) and os.path.isdir(log_dst)):
                raise Exception('Invalid log_dst: %s' % log_dst)
            self.log_dst = log_dst

            if OVERWRITE_LOGS:
                def makeLogSubfolder(parent, name):
                    subfolder = os.path.abspath(os.path.join(parent, name))
                    os.mkdir(subfolder)
                    if not (os.path.exists(subfolder) and os.path.isdir(subfolder)):
                        raise Exception('Invalid log_dst: %s' % log_dst)
                    return subfolder

                self.html_folder = makeLogSubfolder(log_dst, 'html')
                self.css_folder = makeLogSubfolder(self.html_folder, 'stylesheets')
                self.svg_folder = makeLogSubfolder(self.html_folder, 'svg')

                import tfs.common.TFSProject as TFSProject
                srcCssFile = os.path.abspath(os.path.join(TFSProject.findProjectRootFolder(), 'data', 'styles.css'))
                dstCssFile = os.path.abspath(os.path.join(self.css_folder, os.path.basename(srcCssFile)))
                shutil.copy(srcCssFile, dstCssFile)
            else:
                self.html_folder = os.path.join(log_dst, 'html')
                self.css_folder = os.path.join(self.html_folder, 'stylesheets')
                self.svg_folder = os.path.join(self.html_folder, 'svg')

        self.units_per_em = float(self.dstUfoFont.units_per_em)
        self.min_distance = self.min_distance_ems * self.dstUfoFont.units_per_em
        self.max_distance = self.max_distance_ems * self.dstUfoFont.units_per_em
        self.min_non_intrusion  = self.min_non_intrusion_ems * self.dstUfoFont.units_per_em
#        self.rounding = self.rounding_ems * self.dstUfoFont.units_per_em
        print 'self.units_per_em', self.units_per_em
        print 'self.min_distance', self.min_distance
        print 'self.max_distance', self.max_distance
        print 'self.intrusion_tolerance', self.intrusion_tolerance
        print 'self.min_non_intrusion', self.min_non_intrusion
#        print 'self.rounding', self.rounding
    #    kerning.fontMetadata = kerning.ufofont.info

        self.timing = TFTiming()
        self.advanceMap = {}
#        self.minAdvanceMap = defaultdict(0)
        self.rasterCache = {}
        self.srcContoursCache = {}
        self.dstContoursCache = {}
#        self.dstContoursInflateMinDistanceCache = {}
#        self.dstContoursInflateMaxDistanceCache = {}
        self.dstValueCache = {}
        self.srcValueCache = {}
        self.pixelsCache = {}
        minmax = None
        for ufoglyph in self.dstUfoFont.getGlyphs():
#            print 'ufoglyph', ufoglyph.unicode
            contours = self.getGlyphContours(ufoglyph)
            if len(contours) < 1:
                continue
            glyphMinmax = minmaxPaths(contours)
#            print 'glyphMinmax', glyphMinmax
            minmax = minmaxMerge(minmax, glyphMinmax)
#        print 'minmax', minmax
        self.minmax = minmax

#            return [TFSGlyph(glyph) for glyph in self.rffont]

    def updateKerning(self):
        self.dstUfoFont.clearKerning()

        glyphs = self.dstUfoFont.getGlyphs()
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))
        for ufoglyph0 in glyphs:
            for ufoglyph1 in glyphs:
                key = (ufoglyph0.unicode,
                       ufoglyph1.unicode,)
                if key not in self.advanceMap:
                    continue
                advance = self.advanceMap[key]
                advance = int(round(advance))

#                contours0 = self.getGlyphContours(ufoglyph0)
#                contours1 = self.getGlyphContours(ufoglyph1)
#                minmax0 = minmaxPaths(contours0)
#                minmax1 = minmaxPaths(contours1)

                '''
                TODO: add support for re-aligning glyph contours (ie. adjusting side bearings).
                TODO: add support for "max kerning items" argument to limit the number of total kerning values.
                TODO: add support for "min kerning value" argument to ignore small kerning values.
                TODO: add support for controlling what glyphs are kerned (with pairs).
                '''
                kerningValue = advance - ufoglyph0.xAdvance
                if kerningValue != 0:
                    self.dstUfoFont.setKerningPair(ufoglyph0.name,
                                                ufoglyph1.name, kerningValue)
#                    print 'kerning', ufoglyph0.name, ufoglyph1.name, kerningValue, 'advance, ufoglyph0.xAdvance', advance, ufoglyph0.xAdvance


    def clearSideBearings(self):
        '''
        Removes the left and right side bearings from the glyph.
        '''
        glyphs = self.dstUfoFont.getGlyphs()
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))
        for ufoglyph in glyphs:
            if self.isCombiningGlyph(ufoglyph):
                '''
                TODO: Should we normalize the side bearings of these glyphs to perhaps half of max_distance?
                '''
                continue

            contours = self.getGlyphContours(ufoglyph)
#            contours = ufoglyph.getContours()
            if len(contours) == 0:
                '''
                Do not modify width of space and other empty glyphs.
                '''
                continue
            minmax = minmaxPaths(contours)
            contours = [contour.applyPlus(TFSPoint(-minmax.minX, 0)) for contour in contours]
            ufoglyph.setContours(contours, correctDirection=False)
            ufoglyph.setXAdvance(minmax.maxX - minmax.minX)

        # Clear the contours cache.
        self.dstContoursCache = {}
        self.dstValueCache = {}


    def updateSideBearings(self):
        '''
        Rewrite the left and right side bearings of every glyph to be half of the average spacing
        with other glyphs.
        '''

        modifiedAdvanceMap = {}
        modifiedAdvanceMap.update(self.advanceMap)

        '''
        Removes the left and right side bearings from the glyph.
        '''
        glyphs = self.dstUfoFont.getGlyphs()
        glyphs.sort(lambda glyph0, glyph1:cmp(glyph0.unicode, glyph1.unicode))

        glyphWidthMap = {}
        for ufoglyph in glyphs:
            glyphWidthMap[ufoglyph.unicode] = ufoglyph.xAdvance

#        print 'updateSideBearings self.dstContoursCache', self.dstContoursCache.keys()

        for ufoglyph in glyphs:
            if self.isCombiningGlyph(ufoglyph):
                continue
#            print 'updateSideBearings getGlyphContours', ufoglyph.name
            contours = self.getGlyphContours(ufoglyph)
#            contours = ufoglyph.getContours()
            if len(contours) == 0:
                '''
                Do not modify width of space and other empty glyphs.
                '''
                continue

            rightSpacings = []
            rightKeys = []
            leftSpacings = []
            leftKeys = []
            for key in self.advanceMap:
                advance = self.advanceMap[key]
                unicode0, unicode1 = key
                if ufoglyph.unicode == unicode0:
                    '''
                    To get the spacing, subtract the unmodified width of the glyph on the left.
                    '''
                    spacing = advance - glyphWidthMap[unicode0]
                    rightSpacings.append(spacing)
                    rightKeys.append(key)
                elif ufoglyph.unicode == unicode1:
                    '''
                    To get the spacing, subtract the unmodified width of the glyph on the left.
                    '''
                    spacing = advance - glyphWidthMap[unicode0]
                    leftSpacings.append(spacing)
                    leftKeys.append(key)

            '''
            Default sidebearings to half of the "max distance" parameter.
            '''
            leftSideBearing = rightSideBearing = 0.5 * self.max_distance_ems * self.dstUfoFont.units_per_em
            '''
            If we have kerning values for left or right side, use half of the average as the side bearing.
            '''
            if len(rightSpacings) > 0:
                rightSideBearing = 0.5 * reduce(float.__add__, [float(value) for value in rightSpacings]) / len(rightSpacings)
            if len(leftSpacings) > 0:
                leftSideBearing = 0.5 * reduce(float.__add__, [float(value) for value in leftSpacings]) / len(leftSpacings)
            '''
            Use round numbers
            '''
            rightSideBearing = int(round(rightSideBearing))
            leftSideBearing = int(round(leftSideBearing))
            if self.allow_negative_side_bearings:
                '''
                Check that the side bearings are not "negative", ie. do not
                intrude within the glyph bounds.
                '''
                leftSideBearing = max(0, leftSideBearing)
                rightSideBearing = max(0, rightSideBearing)
            '''
            Apply the LSB to the contours.
            '''
            contours = [contour.applyPlus(TFSPoint(+leftSideBearing, 0)) for contour in contours]
            ufoglyph.setContours(contours, correctDirection=False)
            '''
            Update the glyph x advance to reflect the LSB and RSB.
            '''
            ufoglyph.setXAdvance(ufoglyph.xAdvance + leftSideBearing + rightSideBearing)

            '''
            Lastly, update the kerning values in the advance map.
            '''
            for key in leftKeys:
                modifiedAdvanceMap[key] = self.advanceMap[key] - leftSideBearing
            for key in rightKeys:
                modifiedAdvanceMap[key] = self.advanceMap[key] - rightSideBearing

        '''
        Replace the advance map.
        '''
        self.advanceMap = modifiedAdvanceMap


    def assessKerningPair(self, ufoglyph0, ufoglyph1):
        RASTERIZE_CELL_SIZE = self.precision

        contours0 = self.getGlyphContours(ufoglyph0)
        contours1 = self.getGlyphContours(ufoglyph1)
        if (not contours0) or (not contours1):
            return None
        minmax0 = minmaxPaths(contours0)
        minmax1 = minmaxPaths(contours1)

        kerning = self.dstUfoFont.getKerningPair(ufoglyph0.name, ufoglyph1.name)
        if kerning is None:
            kerning = 0
        advance = ufoglyph0.xAdvance + kerning

        pixels0 = self.rasterizeGlyph(ufoglyph0, RASTERIZE_CELL_SIZE)
        pixels1 = self.rasterizeGlyph(ufoglyph1, RASTERIZE_CELL_SIZE)

        if (pixels0 is None) or (pixels1 is None):
            return

        def convertToPixelUnits(value):
            return int(math.ceil(value / float(RASTERIZE_CELL_SIZE)))

        '''
        Find the closest pair of pixels.
        '''
        minDistanceSqrd = None
        for y0, row0 in enumerate(pixels0):
            for x0, pixel0 in enumerate(row0):
                for y1, row1 in enumerate(pixels1):
                    for x1, pixel1 in enumerate(row1):
                        if (not pixel0) or (not pixel1):
                            continue
                        diffX = x0 - (x1 + advance / float(RASTERIZE_CELL_SIZE))
                        diffY = y0 - y1
                        distanceSqrd = (diffX * diffX) + (diffY * diffY)
                        if (minDistanceSqrd is None) or (distanceSqrd < minDistanceSqrd):
                            minDistanceSqrd = distanceSqrd

        if minDistanceSqrd is None:
            return None
        else:
            minDistance = math.sqrt(float(minDistanceSqrd))
            return minDistance * RASTERIZE_CELL_SIZE


    def assessKerning(self):

        glyphs = self.dstUfoFont.getGlyphs()
        unicodeGlyphMap = {}
        for ufoglyph in glyphs:
            if ufoglyph.unicode:
                unicodeGlyphMap[ufoglyph.unicode] = ufoglyph



#        for ufoglyph0 in self.dstUfoFont.getGlyphs():
#            for ufoglyph1 in self.dstUfoFont.getGlyphs():

        pairGroups = (
                      ( min, 'Minimum Distance Pairs',
                         ( ('A', 'A'),
                           ('T', 'T'),
                           ('A', 'V'),
                           ('M', 'M'),
                           ('W', 'W'),
                           ('V', 'V'),
                           ('L', 'L'),
                           ('L', 'J'),
                           ('Y', 'Y'),
                           ('W', 'A'),
                           ('V', 'A'),
                           ('A', 'V'),
                           ('A', 'W'),
                           ),
                         ),
                      ( max, 'Maximum Distance Pairs',
                         ( ('J', 'L'),
                           ('H', 'H'),
                           ('H', 'L'),
                           ('J', 'H'),
                           ('H', 'F'),
                           ('V', 'V'),
                           ('I', 'I'),
                           ('N', 'F'),
                           ('N', 'B'),
                           ('N', 'H'),
                           ('N', 'L'),
                           ('H', 'B'),
                           ('W', 'A'),
                           ('V', 'A'),
                           ('A', 'V'),
                           ('A', 'W'),
                           ),
                         ),
                      )

        def formatEmScalar(value):
            return '%0.3f em' % (value / float(self.units_per_em))

        for reduceFunc, pairGroupName, pairs in pairGroups:
            print
            print pairGroupName
            values = []
            for char0, char1 in pairs:
                unicode0 = ord(char0)
                unicode1 = ord(char1)
#                print 'pair', char0, char1, unicode0, unicode1
                ufoglyph0 = unicodeGlyphMap[unicode0]
                ufoglyph1 = unicodeGlyphMap[unicode1]
                pairDistance = self.assessKerningPair(ufoglyph0, ufoglyph1)
                print 'pair', char0, hex(unicode0), 'vs.', char1, hex(unicode1), 'pairDistance:', pairDistance, ('(%s)' % ( formatEmScalar(pairDistance), ) )
                values.append(pairDistance)
            print pairGroupName, formatEmScalar(reduce(reduceFunc, values))
        print


    def process(self):
        self.configure()

        if self.assess_only:
            print 'Entering assessment mode...'
            self.assessKerning()
            return

        self.timing.mark('configure.')

        if not self.do_not_modify_side_bearings:
            self.clearSideBearings()
            self.timing.mark('clearSideBearings.')

        self.processAllKerningPairs()
        self.timing.mark('processAllKerningPairs.')

#        print 'logDisparities'
        self.logDisparities()
        self.timing.mark('logDisparities.')

        if not self.do_not_modify_side_bearings:
#            print 'updateSideBearings'
            self.updateSideBearings()
            self.timing.mark('updateSideBearings.')

#        print 'updateKerning'
        self.updateKerning()
        self.timing.mark('updateKerning.')

        self.dstUfoFont.update()
        self.dstUfoFont.save(self.ufo_dst)
        self.dstUfoFont.close()

        self.timing.mark('finished.')
        if True:
            self.timing.dump()


if __name__ == "__main__":
    autokern = Autokern()
    AutokernSettings(autokern).getCommandLineSettings()
    autokern.process()

    print
    print 'complete.'
