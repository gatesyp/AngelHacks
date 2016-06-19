//
//  ViewController.swift
//  Dynamic Coursewear
//
//  Created by Aron Gates on 06-18-16.
//  Copyright © 2016 geczy.tech All rights reserved.
//

import UIKit

class ViewController: UIViewController
{
    @IBOutlet var listButton: UIButton!
    @IBOutlet var recordButton: UIButton!
    var whichView = ""
    
    @IBOutlet var lectureButton1: UIButton!
    override func viewDidLoad()
    {
        super.viewDidLoad()
    }
    override func didReceiveMemoryWarning()
    {
        super.didReceiveMemoryWarning()
    }
    
    // Overlay Record
    lazy var recordView: RecordViewController = {
        let recordView = RecordViewController()
        return recordView
    }()
    
    // Overlay List
    lazy var listView: ListViewController = {
        let listView = ListViewController()
        return listView
    }()
    
    // Overlay Upload
    lazy var uploadView: UploadViewController = {
        let uploadView = UploadViewController()
        return uploadView
    }()
    
    @IBAction func recordViewPress()
    {
        if whichView != "recordView"
        {
            home()
            whichView = "recordView"
            recordView.displayView(view)
        }
    }
    
    @IBAction func listViewPress()
    {
        if whichView != "listView"
        {
            home()
            whichView = "listView"
            listView.displayView(view)
        }
    }
    
    @IBAction func uploadViewPress()
    {
        if whichView != "uploadView"
        {
            home()
            whichView = "uploadView"
            uploadView.displayView(view)
        }
    }
    
    @IBAction func homeViewPress()
    {
        home()
        whichView = ""
    }
    
    func home()
    {
        switch whichView
        {
        case "recordView":
            recordView.hideView()
            break
        case "listView":
            listView.hideView()
            break
        case "uploadView":
            uploadView.hideView()
            break
        default:
            break
        }
    }
    
    @IBAction func chooseLecture()
    {
        if lectureButton1.currentTitleColor == #colorLiteral(red: 0, green: 0, blue: 0, alpha: 1)
        {
            lectureButton1.setTitleColor(#colorLiteral(red: 0.09803923219, green: 0.3607843518, blue: 0.3098038435, alpha: 1), for: [])
        }
        else
        {
            lectureButton1.setTitleColor(#colorLiteral(red: 0, green: 0, blue: 0, alpha: 1), for: [])
        }
    }

}
