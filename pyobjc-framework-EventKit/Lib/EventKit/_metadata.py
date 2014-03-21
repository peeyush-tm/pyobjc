# This file is generated by objective.metadata
#
# Last update: Wed Sep 19 17:29:42 2012

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
constants = '''$EKErrorDomain$EKEventStoreChangedNotification$'''
enums = '''$EKAlarmProximityEnter@1$EKAlarmProximityLeave@2$EKAlarmProximityNone@0$EKAlarmTypeAudio@1$EKAlarmTypeDisplay@0$EKAlarmTypeEmail@3$EKAlarmTypeProcedure@2$EKCalendarEventAvailabilityBusy@1$EKCalendarEventAvailabilityFree@2$EKCalendarEventAvailabilityNone@0$EKCalendarEventAvailabilityTentative@4$EKCalendarEventAvailabilityUnavailable@8$EKCalendarTypeBirthday@4$EKCalendarTypeCalDAV@1$EKCalendarTypeExchange@2$EKCalendarTypeLocal@0$EKCalendarTypeSubscription@3$EKEntityMaskEvent@1$EKEntityMaskReminder@2$EKEntityTypeEvent@0$EKEntityTypeReminder@1$EKErrorAlarmGreaterThanRecurrence@8$EKErrorAlarmProximityNotSupported@21$EKErrorCalendarDoesNotAllowEvents@22$EKErrorCalendarDoesNotAllowReminders@23$EKErrorCalendarHasNoSource@14$EKErrorCalendarIsImmutable@16$EKErrorCalendarReadOnly@6$EKErrorCalendarSourceCannotBeModified@15$EKErrorDatesInverted@4$EKErrorDurationGreaterThanRecurrence@7$EKErrorEventNotMutable@0$EKErrorInternalFailure@5$EKErrorInvalidSpan@13$EKErrorInvitesCannotBeMoved@12$EKErrorLast@26$EKErrorNoCalendar@1$EKErrorNoEndDate@3$EKErrorNoStartDate@2$EKErrorObjectBelongsToDifferentStore@11$EKErrorRecurringReminderRequiresDueDate@18$EKErrorReminderLocationsNotSupported@20$EKErrorSourceDoesNotAllowCalendarAddDelete@17$EKErrorSourceDoesNotAllowEvents@25$EKErrorSourceDoesNotAllowReminders@24$EKErrorStartDateCollidesWithOtherOccurrence@10$EKErrorStartDateTooFarInFuture@9$EKErrorStructuredLocationsNotSupported@19$EKEventAvailabilityBusy@0$EKEventAvailabilityFree@1$EKEventAvailabilityNotSupported@-1$EKEventAvailabilityTentative@2$EKEventAvailabilityUnavailable@3$EKEventStatusCanceled@3$EKEventStatusConfirmed@1$EKEventStatusNone@0$EKEventStatusTentative@2$EKFriday@6$EKMonday@2$EKParticipantRoleChair@3$EKParticipantRoleNonParticipant@4$EKParticipantRoleOptional@2$EKParticipantRoleRequired@1$EKParticipantRoleUnknown@0$EKParticipantStatusAccepted@2$EKParticipantStatusCompleted@6$EKParticipantStatusDeclined@3$EKParticipantStatusDelegated@5$EKParticipantStatusInProcess@7$EKParticipantStatusPending@1$EKParticipantStatusTentative@4$EKParticipantStatusUnknown@0$EKParticipantTypeGroup@4$EKParticipantTypePerson@1$EKParticipantTypeResource@3$EKParticipantTypeRoom@2$EKParticipantTypeUnknown@0$EKRecurrenceFrequencyDaily@0$EKRecurrenceFrequencyMonthly@2$EKRecurrenceFrequencyWeekly@1$EKRecurrenceFrequencyYearly@3$EKSaturday@7$EKSourceTypeBirthdays@5$EKSourceTypeCalDAV@2$EKSourceTypeExchange@1$EKSourceTypeLocal@0$EKSourceTypeMobileMe@3$EKSourceTypeSubscribed@4$EKSpanFutureEvents@1$EKSpanThisEvent@0$EKSunday@1$EKThursday@5$EKTuesday@3$EKWednesday@4$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'EKCalendar', b'allowsContentModifications', {'retval': {'type': b'Z'}})
    r(b'EKCalendar', b'isImmutable', {'retval': {'type': b'Z'}})
    r(b'EKCalendar', b'isSubscribed', {'retval': {'type': b'Z'}})
    r(b'EKCalendarItem', b'hasAlarms', {'retval': {'type': b'Z'}})
    r(b'EKCalendarItem', b'hasAttendees', {'retval': {'type': b'Z'}})
    r(b'EKCalendarItem', b'hasNotes', {'retval': {'type': b'Z'}})
    r(b'EKCalendarItem', b'hasRecurrenceRules', {'retval': {'type': b'Z'}})
    r(b'EKCalendarItem', b'isAllDay', {'retval': {'type': 'Z'}})
    r(b'EKEvent', b'isAllDay', {'retval': {'type': b'Z'}})
    r(b'EKEvent', b'isDetached', {'retval': {'type': b'Z'}})
    r(b'EKEvent', b'refresh', {'retval': {'type': b'Z'}})
    r(b'EKEvent', b'setAllDay:', {'arguments': {2: {'type': b'Z'}}})
    r(b'EKEventStore', b'commit:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r(b'EKEventStore', b'enumerateEventsMatchingPredicate:usingBlock:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'o^B'}}}}}})
    r(b'EKEventStore', b'fetchRemindersMatchingPredicate:completion:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'EKEventStore', b'removeCalendar:commit:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'Z'}, 4: {'type_modifier': b'o'}}})
    r(b'EKEventStore', b'removeEvent:span:commit:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type': b'Z'}, 5: {'type_modifier': b'o'}}})
    r(b'EKEventStore', b'removeReminder:commit:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'Z'}, 4: {'type_modifier': b'o'}}})
    r(b'EKEventStore', b'saveCalendar:commit:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'Z'}, 4: {'type_modifier': b'o'}}})
    r(b'EKEventStore', b'saveEvent:span:commit:error:', {'retval': {'type': b'Z'}, 'arguments': {4: {'type': b'Z'}, 5: {'type_modifier': b'o'}}})
    r(b'EKEventStore', b'saveReminder:commit:error:', {'retval': {'type': b'Z'}, 'arguments': {3: {'type': b'Z'}, 4: {'type_modifier': b'o'}}})
    r(b'EKObject', b'hasChanges', {'retval': {'type': b'Z'}})
    r(b'EKObject', b'isNew', {'retval': {'type': b'Z'}})
    r(b'EKObject', b'refresh', {'retval': {'type': b'Z'}})
    r(b'EKReminder', b'isCompleted', {'retval': {'type': b'Z'}})
    r(b'EKReminder', b'setCompleted:', {'arguments': {2: {'type': b'Z'}}})
finally:
    objc._updatingMetadata(False)
expressions = {'DATE_COMPONENTS': '(NSEraCalendarUnit | NSYearCalendarUnit | NSMonthCalendarUnit | NSDayCalendarUnit)'}

# END OF FILE
