//
//  TestObject.h
//  Test
//
//  Created by 黄文希 on 2018/10/30.
//  Copyright © 2018 Hays. All rights reserved.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface TestObject : NSObject

- (void)log;

- (void)showLog:(NSString *)text;

- (void)addView:(id)view;

@end

NS_ASSUME_NONNULL_END
