/*
 * Helper tool for converting an NSArchive or NSKeyedArchive
 * to a plist on stdout.
 */
#import <Foundation/Foundation.h>
#include <stdio.h>

int main(int argc, char** argv)
{
    int keyed;
    NSAutoreleasePool* pool = [[NSAutoreleasePool alloc] init];

    if (argc != 3) {
        printf("Usage: dump-nsarchive <plain|keyed> FILE\n");
        return 1;
    }

    if (strcmp(argv[1], "plain") == 0) {
        keyed = 0;
    } else if (strcmp(argv[1], "keyed") == 0) {
        keyed = 1;
    } else {
        printf("Usage: dump-nsarchive <plain|keyed> FILE\n");
        return 1;
    }

    NSString* path = [[NSString alloc] initWithUTF8String:argv[2]];
    NSObject* value;

    @try {
        if (keyed) {
            value = [NSKeyedUnarchiver unarchiveObjectWithFile:path];

        } else {
            value = [NSUnarchiver unarchiveObjectWithFile:path];
        }
    } @catch (NSException* localException) {
        printf("Exception during unarchiving: %s\n", [[localException description] UTF8String]);
        return 2;
    }

    [path release];

    if (value == nil) {
        printf("Cannot decode archive\n");
        return 2;
    }

#if PyObjC_BUILD_RELEASE >= 1006
    NSError* error = nil;
    NSData* data = [NSPropertyListSerialization
        dataWithPropertyList:value
                      format:NSPropertyListXMLFormat_v1_0
                     options:NSPropertyListMutableContainersAndLeaves
                       error:&error];
#else
    NSString* error = nil;
    NSData* data = [NSPropertyListSerialization
        dataFromPropertyList:value
                      format:NSPropertyListXMLFormat_v1_0
                       errorDescription:&error];
#endif

    if (data == nil) {
        /* Some types we test cannot be represented as a plist */
        printf("%s\n", [[value description] UTF8String]);
        return 0;
    }

    fwrite([data bytes], 1, [data length], stdout);
    return 0;
}
