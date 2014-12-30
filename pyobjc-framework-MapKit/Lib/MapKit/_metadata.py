# This file is generated by objective.metadata
#
# Last update: Tue Dec 30 22:10:14 2014

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
misc.update({'MKMapRect': objc.createStructType('MKMapRect', b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}', ['origin', 'size']), 'MKMapSize': objc.createStructType('MKMapSize', b'{_MKMapSize=dd}', ['width', 'height']), 'MKCoordinateRegion': objc.createStructType('MKCoordinateRegion', b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}', ['center', 'span']), 'MKCoordinateSpan': objc.createStructType('MKCoordinateSpan', b'{_MKCoordinateSpan=dd}', ['latitudeDelta', 'longitudeDelta']), 'MKTileOverlayPath': objc.createStructType('MKTileOverlayPath', b'{_MKTileOverlayPath=qqqd}', ['x', 'y', 'z', 'contentScaleFactor']), 'MKMapPoint': objc.createStructType('MKMapPoint', b'{_MKMapPoint=dd}', ['x', 'y'])})
constants = '''$MKAnnotationCalloutInfoDidChangeNotification$MKErrorDomain$MKLaunchOptionsCameraKey$MKLaunchOptionsDirectionsModeDriving$MKLaunchOptionsDirectionsModeKey$MKLaunchOptionsDirectionsModeWalking$MKLaunchOptionsMapCenterKey$MKLaunchOptionsMapSpanKey$MKLaunchOptionsMapTypeKey$MKLaunchOptionsShowsTrafficKey$MKMapRectNull@{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}$MKMapRectWorld@{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}$MKMapSizeWorld@{_MKMapSize=dd}$'''
enums = '''$MKAnnotationViewDragStateCanceling@3$MKAnnotationViewDragStateDragging@2$MKAnnotationViewDragStateEnding@4$MKAnnotationViewDragStateNone@0$MKAnnotationViewDragStateStarting@1$MKDirectionsTransportTypeAny@268435455$MKDirectionsTransportTypeAutomobile@1$MKDirectionsTransportTypeWalking@2$MKDistanceFormatterUnitStyleAbbreviated@1$MKDistanceFormatterUnitStyleDefault@0$MKDistanceFormatterUnitStyleFull@2$MKDistanceFormatterUnitsDefault@0$MKDistanceFormatterUnitsImperial@2$MKDistanceFormatterUnitsImperialWithYards@3$MKDistanceFormatterUnitsMetric@1$MKErrorDirectionsNotFound@5$MKErrorLoadingThrottled@3$MKErrorPlacemarkNotFound@4$MKErrorServerFailure@2$MKErrorUnknown@1$MKMapTypeHybrid@2$MKMapTypeSatellite@1$MKMapTypeStandard@0$MKOverlayLevelAboveLabels@1$MKOverlayLevelAboveRoads@0$MKPinAnnotationColorGreen@1$MKPinAnnotationColorPurple@2$MKPinAnnotationColorRed@0$MKUserTrackingModeFollow@1$MKUserTrackingModeFollowWithHeading@2$MKUserTrackingModeNone@0$'''
misc.update({})
functions={'MKMapRectOffset': (b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}dd',), 'MKMapRectIsEmpty': (b'Z{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKMapRectGetMidX': (b'd{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKMapRectGetMidY': (b'd{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKMapRectGetMinX': (b'd{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKMapRectGetWidth': (b'd{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKStringFromMapRect': (b'@{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKCoordinateSpanMake': (b'{_MKCoordinateSpan=dd}dd',), 'MKMapRectGetMaxX': (b'd{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKMapRectGetMaxY': (b'd{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKMapSizeEqualToSize': (b'Z{_MKMapSize=dd}{_MKMapSize=dd}',), 'MKMapRectIsNull': (b'Z{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKStringFromMapPoint': (b'@{_MKMapPoint=dd}',), 'MKMapRectDivide': (b'v{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}^{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}^{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}dI', '', {'arguments': {1: {'type_modifier': 'o'}, 2: {'type_modifier': 'o'}}}), 'MKMetersPerMapPointAtLatitude': (b'dd',), 'MKCoordinateRegionMakeWithDistance': (b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}{_CLLocationCoordinate2D=dd}dd',), 'MKMapRectMake': (b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}dddd',), 'MKMapPointEqualToPoint': (b'Z{_MKMapPoint=dd}{_MKMapPoint=dd}',), 'MKMapRectContainsPoint': (b'Z{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}{_MKMapPoint=dd}',), 'MKMapRectUnion': (b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKCoordinateForMapPoint': (b'{_CLLocationCoordinate2D=dd}{_MKMapPoint=dd}',), 'MKMapRectRemainder': (b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKCoordinateRegionMake': (b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}{_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}',), 'MKStringFromMapSize': (b'@{_MKMapSize=dd}',), 'MKCoordinateRegionForMapRect': (b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKMapSizeMake': (b'{_MKMapSize=dd}dd',), 'MKMapRectIntersection': (b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKMapRectInset': (b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}dd',), 'MKMapRectContainsRect': (b'Z{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKMapRectGetMinY': (b'd{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKRoadWidthAtZoomScale': (b'dd',), 'MKMapRectSpans180thMeridian': (b'Z{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKMapPointForCoordinate': (b'{_MKMapPoint=dd}{_CLLocationCoordinate2D=dd}',), 'MKMapPointsPerMeterAtLatitude': (b'dd',), 'MKMapRectIntersectsRect': (b'Z{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKMetersBetweenMapPoints': (b'd{_MKMapPoint=dd}{_MKMapPoint=dd}',), 'MKMapPointMake': (b'{_MKMapPoint=dd}dd',), 'MKMapRectEqualToRect': (b'Z{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',), 'MKMapRectGetHeight': (b'd{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}',)}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'MKAnnotationView', b'canShowCallout', {'retval': {'type': b'Z'}})
    r(b'MKAnnotationView', b'isDraggable', {'retval': {'type': b'Z'}})
    r(b'MKAnnotationView', b'isEnabled', {'retval': {'type': b'Z'}})
    r(b'MKAnnotationView', b'isHighlighted', {'retval': {'type': b'Z'}})
    r(b'MKAnnotationView', b'isSelected', {'retval': {'type': b'Z'}})
    r(b'MKAnnotationView', b'setCanShowCallout:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKAnnotationView', b'setDragState:animated:', {'arguments': {3: {'type': b'Z'}}})
    r(b'MKAnnotationView', b'setDraggable:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKAnnotationView', b'setEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKAnnotationView', b'setHighlighted:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKAnnotationView', b'setSelected:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKAnnotationView', b'setSelected:animated:', {'arguments': {2: {'type': b'Z'}, 3: {'type': b'Z'}}})
    r(b'MKCircle', b'boundingMapRect', {'retval': {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}})
    r(b'MKCircle', b'circleWithCenterCoordinate:radius:', {'arguments': {2: {'type': b'{_CLLocationCoordinate2D=dd}'}}})
    r(b'MKCircle', b'circleWithMapRect:', {'arguments': {2: {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}}})
    r(b'MKCircle', b'coordinate', {'retval': {'type': b'{_CLLocationCoordinate2D=dd}'}})
    r(b'MKDirections', b'calculateDirectionsWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'MKDirections', b'calculateETAWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'MKDirections', b'isCalculating', {'retval': {'type': b'Z'}})
    r(b'MKDirectionsRequest', b'isDirectionsRequestURL:', {'retval': {'type': b'Z'}})
    r(b'MKDirectionsRequest', b'requestsAlternateRoutes', {'retval': {'type': b'Z'}})
    r(b'MKDirectionsRequest', b'setRequestsAlternateRoutes:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKGeodesicPolyline', b'polylineWithCoordinates:count:', {'arguments': {2: {'type': b'^{_CLLocationCoordinate2D=dd}', 'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'MKGeodesicPolyline', b'polylineWithPoints:count:', {'arguments': {2: {'type': b'^{_MKMapPoint=dd}', 'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'MKLocalSearch', b'isSearching', {'retval': {'type': b'Z'}})
    r(b'MKLocalSearch', b'startWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'MKLocalSearchRequest', b'region', {'retval': {'type': b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}'}})
    r(b'MKLocalSearchRequest', b'setRegion:', {'arguments': {2: {'type': b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}'}}})
    r(b'MKLocalSearchResponse', b'boundingRegion', {'retval': {'type': b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}'}})
    r(b'MKMapCamera', b'cameraLookingAtCenterCoordinate:fromEyeCoordinate:eyeAltitude:', {'arguments': {2: {'type': b'{_CLLocationCoordinate2D=dd}'}, 3: {'type': b'{_CLLocationCoordinate2D=dd}'}}})
    r(b'MKMapCamera', b'centerCoordinate', {'retval': {'type': b'{_CLLocationCoordinate2D=dd}'}})
    r(b'MKMapCamera', b'setCenterCoordinate:', {'arguments': {2: {'type': b'{_CLLocationCoordinate2D=dd}'}}})
    r(b'MKMapItem', b'isCurrentLocation', {'retval': {'type': b'Z'}})
    r(b'MKMapItem', b'openInMapsWithLaunchOptions:', {'retval': {'type': b'Z'}})
    r(b'MKMapItem', b'openMapsWithItems:launchOptions:', {'retval': {'type': b'Z'}})
    r(b'MKMapSnapshot', b'pointForCoordinate:', {'arguments': {2: {'type': b'{_CLLocationCoordinate2D=dd}'}}})
    r(b'MKMapSnapshotOptions', b'mapRect', {'retval': {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}})
    r(b'MKMapSnapshotOptions', b'region', {'retval': {'type': b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}'}})
    r(b'MKMapSnapshotOptions', b'setMapRect:', {'arguments': {2: {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}}})
    r(b'MKMapSnapshotOptions', b'setRegion:', {'arguments': {2: {'type': b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}'}}})
    r(b'MKMapSnapshotOptions', b'setShowsBuildings:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKMapSnapshotOptions', b'setShowsPointsOfInterest:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKMapSnapshotOptions', b'showsBuildings', {'retval': {'type': b'Z'}})
    r(b'MKMapSnapshotOptions', b'showsPointsOfInterest', {'retval': {'type': b'Z'}})
    r(b'MKMapSnapshotter', b'isLoading', {'retval': {'type': b'Z'}})
    r(b'MKMapSnapshotter', b'startWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'MKMapSnapshotter', b'startWithQueue:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'MKMapView', b'annotationsInMapRect:', {'arguments': {2: {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}}})
    r(b'MKMapView', b'centerCoordinate', {'retval': {'type': b'{_CLLocationCoordinate2D=dd}'}})
    r(b'MKMapView', b'convertCoordinate:toPointToView:', {'arguments': {2: {'type': b'{_CLLocationCoordinate2D=dd}'}}})
    r(b'MKMapView', b'convertPoint:toCoordinateFromView:', {'retval': {'type': b'{_CLLocationCoordinate2D=dd}'}})
    r(b'MKMapView', b'convertRect:toRegionFromView:', {'retval': {'type': b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}'}})
    r(b'MKMapView', b'convertRegion:toRectToView:', {'arguments': {2: {'type': b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}'}}})
    r(b'MKMapView', b'deselectAnnotation:animated:', {'arguments': {3: {'type': b'Z'}}})
    r(b'MKMapView', b'isPitchEnabled', {'retval': {'type': b'Z'}})
    r(b'MKMapView', b'isRotateEnabled', {'retval': {'type': b'Z'}})
    r(b'MKMapView', b'isScrollEnabled', {'retval': {'type': b'Z'}})
    r(b'MKMapView', b'isUserLocationVisible', {'retval': {'type': b'Z'}})
    r(b'MKMapView', b'isZoomEnabled', {'retval': {'type': b'Z'}})
    r(b'MKMapView', b'mapRectThatFits:', {'retval': {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}, 'arguments': {2: {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}}})
    r(b'MKMapView', b'mapRectThatFits:edgePadding:', {'retval': {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}, 'arguments': {2: {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}, 3: {'type': b'{_NSEdgeInsets=dddd}'}}})
    r(b'MKMapView', b'region', {'retval': {'type': b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}'}})
    r(b'MKMapView', b'regionThatFits:', {'retval': {'type': b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}'}, 'arguments': {2: {'type': b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}'}}})
    r(b'MKMapView', b'selectAnnotation:animated:', {'arguments': {3: {'type': b'Z'}}})
    r(b'MKMapView', b'setCamera:animated:', {'arguments': {3: {'type': b'Z'}}})
    r(b'MKMapView', b'setCenterCoordinate:', {'arguments': {2: {'type': b'{_CLLocationCoordinate2D=dd}'}}})
    r(b'MKMapView', b'setCenterCoordinate:animated:', {'arguments': {2: {'type': b'{_CLLocationCoordinate2D=dd}'}, 3: {'type': b'Z'}}})
    r(b'MKMapView', b'setPitchEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKMapView', b'setRegion:', {'arguments': {2: {'type': b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}'}}})
    r(b'MKMapView', b'setRegion:animated:', {'arguments': {2: {'type': b'{_MKCoordinateRegion={_CLLocationCoordinate2D=dd}{_MKCoordinateSpan=dd}}'}, 3: {'type': b'Z'}}})
    r(b'MKMapView', b'setRotateEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKMapView', b'setScrollEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKMapView', b'setShowsBuildings:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKMapView', b'setShowsCompass:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKMapView', b'setShowsPointsOfInterest:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKMapView', b'setShowsScale:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKMapView', b'setShowsUserLocation:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKMapView', b'setShowsZoomControls:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKMapView', b'setVisibleMapRect:', {'arguments': {2: {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}}})
    r(b'MKMapView', b'setVisibleMapRect:animated:', {'arguments': {2: {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}, 3: {'type': b'Z'}}})
    r(b'MKMapView', b'setVisibleMapRect:edgePadding:animated:', {'arguments': {2: {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}, 3: {'type': b'{_NSEdgeInsets=dddd}'}, 4: {'type': b'Z'}}})
    r(b'MKMapView', b'setZoomEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKMapView', b'showAnnotations:animated:', {'arguments': {3: {'type': b'Z'}}})
    r(b'MKMapView', b'showsBuildings', {'retval': {'type': b'Z'}})
    r(b'MKMapView', b'showsCompass', {'retval': {'type': b'Z'}})
    r(b'MKMapView', b'showsPointsOfInterest', {'retval': {'type': b'Z'}})
    r(b'MKMapView', b'showsScale', {'retval': {'type': b'Z'}})
    r(b'MKMapView', b'showsUserLocation', {'retval': {'type': b'Z'}})
    r(b'MKMapView', b'showsZoomControls', {'retval': {'type': b'Z'}})
    r(b'MKMapView', b'visibleMapRect', {'retval': {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}})
    r(b'MKMultiPoint', b'getCoordinates:range:', {'arguments': {2: {'type': b'^{_CLLocationCoordinate2D=dd}', 'type_modifier': b'o', 'c_array_length_in_arg': 3}}})
    r(b'MKMultiPoint', b'points', {'retval': {'type': b'^{_MKMapPoint=dd}', 'c_array_of_variable_length': True}})
    r(b'MKOverlayRenderer', b'canDrawMapRect:zoomScale:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}}})
    r(b'MKOverlayRenderer', b'drawMapRect:zoomScale:inContext:', {'arguments': {2: {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}}})
    r(b'MKOverlayRenderer', b'mapPointForPoint:', {'retval': {'type': b'{_MKMapPoint=dd}'}})
    r(b'MKOverlayRenderer', b'mapRectForRect:', {'retval': {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}})
    r(b'MKOverlayRenderer', b'pointForMapPoint:', {'arguments': {2: {'type': b'{_MKMapPoint=dd}'}}})
    r(b'MKOverlayRenderer', b'rectForMapRect:', {'arguments': {2: {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}}})
    r(b'MKOverlayRenderer', b'setNeedsDisplayInMapRect:', {'arguments': {2: {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}}})
    r(b'MKOverlayRenderer', b'setNeedsDisplayInMapRect:zoomScale:', {'arguments': {2: {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}}})
    r(b'MKPinAnnotationView', b'animatesDrop', {'retval': {'type': b'Z'}})
    r(b'MKPinAnnotationView', b'setAnimatesDrop:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKPlacemark', b'initWithCoordinate:addressDictionary:', {'arguments': {2: {'type': b'{_CLLocationCoordinate2D=dd}'}}})
    r(b'MKPointAnnotation', b'coordinate', {'retval': {'type': b'{_CLLocationCoordinate2D=dd}'}})
    r(b'MKPointAnnotation', b'setCoordinate:', {'arguments': {2: {'type': b'{_CLLocationCoordinate2D=dd}'}}})
    r(b'MKPolygon', b'polygonWithCoordinates:count:', {'arguments': {2: {'type': b'^{_CLLocationCoordinate2D=dd}', 'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'MKPolygon', b'polygonWithCoordinates:count:interiorPolygons:', {'arguments': {2: {'type': b'^{_CLLocationCoordinate2D=dd}', 'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'MKPolygon', b'polygonWithPoints:count:', {'arguments': {2: {'type': b'^{_MKMapPoint=dd}', 'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'MKPolygon', b'polygonWithPoints:count:interiorPolygons:', {'arguments': {2: {'type': b'^{_MKMapPoint=dd}', 'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'MKPolyline', b'polylineWithCoordinates:count:', {'arguments': {2: {'type': b'^{_CLLocationCoordinate2D=dd}', 'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'MKPolyline', b'polylineWithPoints:count:', {'arguments': {2: {'type': b'^{_MKMapPoint=dd}', 'type_modifier': b'n', 'c_array_length_in_arg': 3}}})
    r(b'MKTileOverlay', b'URLForTilePath:', {'arguments': {2: {'type': b'{_MKTileOverlayPath=qqqd}'}}})
    r(b'MKTileOverlay', b'canReplaceMapContent', {'retval': {'type': b'Z'}})
    r(b'MKTileOverlay', b'isGeometryFlipped', {'retval': {'type': b'Z'}})
    r(b'MKTileOverlay', b'loadTileAtPath:result:', {'arguments': {2: {'type': b'{_MKTileOverlayPath=qqqd}'}, 3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'MKTileOverlay', b'setCanReplaceMapContent:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKTileOverlay', b'setGeometryFlipped:', {'arguments': {2: {'type': b'Z'}}})
    r(b'MKUserLocation', b'isUpdating', {'retval': {'type': b'Z'}})
    r(b'NSValue', b'MKCoordinateSpanValue', {'retval': {'type': b'{_MKCoordinateSpan=dd}'}})
    r(b'NSValue', b'MKCoordinateValue', {'retval': {'type': b'{_CLLocationCoordinate2D=dd}'}})
    r(b'NSValue', b'valueWithMKCoordinate:', {'arguments': {2: {'type': b'{_CLLocationCoordinate2D=dd}'}}})
    r(b'NSValue', b'valueWithMKCoordinateSpan:', {'arguments': {2: {'type': b'{_MKCoordinateSpan=dd}'}}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'boundingMapRect', {'required': True, 'retval': {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}})
    r(b'NSObject', b'canReplaceMapContent', {'required': False, 'retval': {'type': b'Z'}})
    r(b'NSObject', b'coordinate', {'required': True, 'retval': {'type': b'{_CLLocationCoordinate2D=dd}'}})
    r(b'NSObject', b'coordinate', {'required': True, 'retval': {'type': b'{_CLLocationCoordinate2D=dd}'}})
    r(b'NSObject', b'intersectsMapRect:', {'required': False, 'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'{_MKMapRect={_MKMapPoint=dd}{_MKMapSize=dd}}'}}})
    r(b'NSObject', b'mapView:annotationView:didChangeDragState:fromOldState:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'Q'}, 5: {'type': b'Q'}}})
    r(b'NSObject', b'mapView:didAddAnnotationViews:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'mapView:didAddOverlayRenderers:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'mapView:didDeselectAnnotationView:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'mapView:didFailToLocateUserWithError:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'mapView:didSelectAnnotationView:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'mapView:didUpdateUserLocation:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'mapView:regionDidChangeAnimated:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'Z'}}})
    r(b'NSObject', b'mapView:regionWillChangeAnimated:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'Z'}}})
    r(b'NSObject', b'mapView:rendererForOverlay:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'mapView:viewForAnnotation:', {'required': False, 'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'mapViewDidFailLoadingMap:withError:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'mapViewDidFinishLoadingMap:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'mapViewDidFinishRenderingMap:fullyRendered:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'Z'}}})
    r(b'NSObject', b'mapViewDidStopLocatingUser:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'mapViewWillStartLoadingMap:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'mapViewWillStartLocatingUser:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'mapViewWillStartRenderingMap:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'setCoordinate:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'{_CLLocationCoordinate2D=dd}'}}})
    r(b'NSObject', b'subtitle', {'required': False, 'retval': {'type': b'@'}})
    r(b'NSObject', b'title', {'required': False, 'retval': {'type': b'@'}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
